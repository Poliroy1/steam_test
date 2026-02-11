import random
import time
from uuid import uuid4

import pytest
import requests
from services.auth.auth_service import AuthService
from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest
from services.university.models.base_grade import BaseGrade
from services.university.models.base_student import DegreeEnum
from services.university.models.base_teacher import SubjectEnum
from services.university.models.grade_request import GradeRequest
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService
from services.university.models.base_grade import MIN_GRADE, MAX_GRADE
from utils.api_utils import ApiUtils
from faker import Faker

faker = Faker()


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_anonym():
    api_utils = ApiUtils(url=AuthService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_anonym():
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def access_token(auth_api_utils_anonym):
    auth_service = AuthService(auth_api_utils_anonym)
    username = faker.user_name()
    password = faker.password(length=30,
                              special_chars=True,
                              digits=True,
                              upper_case=True,
                              lower_case=True)
    auth_service.register_user(
        register_request=RegisterRequest(
            username=username,
            password=password,
            password_repeat=password,
            email=faker.email()))
    login_response = auth_service.login_user(login_request=LoginRequest(
        username=username,
        password=password
    ))

    return login_response.access_token


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_admin(access_token):
    api_utils = ApiUtils(url=AuthService.SERVICE_URL,
                         headers={"Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_admin(access_token):
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL,
                         headers={"Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def create_group(university_api_utils_admin):
    university_service = UniversityService(university_api_utils_admin)
    group = GroupRequest(name=faker.name())
    group_response = university_service.create_group(group)
    return group_response


@pytest.fixture(scope="function", autouse=False)
def create_student(university_api_utils_admin, create_group):
    university_service = UniversityService(api_utils=university_api_utils_admin)
    student = StudentRequest(first_name=faker.first_name(),
                             last_name=faker.last_name(),
                             degree=random.choice([option for option in DegreeEnum]),
                             phone=faker.numerify('+7##########'),
                             email=faker.email(),
                             group_id=create_group.id)
    student_response = university_service.create_student(student)
    return student_response


@pytest.fixture(scope="function", autouse=False)
def create_teacher(university_api_utils_admin):
    university_service = UniversityService(api_utils=university_api_utils_admin)
    teacher = TeacherRequest(first_name=faker.first_name(), last_name=faker.last_name(),
                             subject=random.choice([option for option in SubjectEnum]), )
    teacher_response = university_service.create_teacher(teacher)
    return teacher_response

@pytest.fixture(scope="function")
def create_grade(university_api_utils_admin, create_teacher, create_student):
    university_service = UniversityService(api_utils=university_api_utils_admin)
    grade = GradeRequest(
        teacher_id=create_teacher.id,
        student_id=create_student.id,
        grade=random.randint(MIN_GRADE, MAX_GRADE))

    grade_response = university_service.create_grade(grade_request=grade)
    return grade_response

@pytest.fixture
def student_payload(create_group):
    return StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        degree=random.choice([d for d in DegreeEnum]),
        phone=faker.numerify("+7##########"),
        email=faker.email(),
        group_id=create_group.id
    )

@pytest.fixture
def university_service(university_api_utils_admin):
    return UniversityService(api_utils=university_api_utils_admin)

@pytest.fixture
def grade_stats_dataset(university_service):
    group_a = university_service.create_group(GroupRequest(name=f"group_a_{uuid4().hex[:8]}"))
    group_b = university_service.create_group(GroupRequest(name=f"group_b_{uuid4().hex[:8]}"))

    student_a1 = university_service.create_student(StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        degree=random.choice([o for o in DegreeEnum]),
        phone=faker.numerify("+7##########"),
        email=faker.email(),
        group_id=group_a.id,
    ))
    student_a2 = university_service.create_student(StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        degree=random.choice([o for o in DegreeEnum]),
        phone=faker.numerify("+7##########"),
        email=faker.email(),
        group_id=group_a.id,
    ))
    student_b1 = university_service.create_student(StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        degree=random.choice([o for o in DegreeEnum]),
        phone=faker.numerify("+7##########"),
        email=faker.email(),
        group_id=group_b.id,
    ))

    teacher_main = university_service.create_teacher(TeacherRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        subject=random.choice([o for o in SubjectEnum]),
    ))
    teacher_other = university_service.create_teacher(TeacherRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        subject=random.choice([o for o in SubjectEnum]),
    ))

    grade_a = university_service.create_random_grade(teacher_main.id, student_a1.id).grade
    grade_b = university_service.create_random_grade(teacher_main.id, student_a1.id).grade
    grade_c = university_service.create_random_grade(teacher_main.id, student_a2.id).grade

    _unrelated_grade = university_service.create_random_grade(teacher_other.id, student_b1.id).grade

    expected_by_student_a1 = [grade_a, grade_b]
    expected_by_teacher_main = [grade_a, grade_b, grade_c]
    expected_by_group_a = [grade_a, grade_b, grade_c]

    return {
        "groups": {"a": group_a, "b": group_b},
        "students": {"a1": student_a1, "a2": student_a2, "b1": student_b1},
        "teachers": {"main": teacher_main, "other": teacher_other},
        "expected": {
            "by_student_a1": expected_by_student_a1,
            "by_teacher_main": expected_by_teacher_main,
            "by_group_a": expected_by_group_a,
        },
    }

@pytest.fixture(scope="session", autouse=True)
def auth_service_readiness():
    timeout = 180
    start_time = time.time()
    while time.time() < start_time + timeout:
        try:
            response = requests.get(AuthService.SERVICE_URL + "/docs")
            response.raise_for_status()
        except requests.exceptions.ConnectionError:
            time.sleep(1)
        else:
            break
    else:
        raise RuntimeError(f"Auth service wasn't started during '{timeout}' seconds.' ")


@pytest.fixture(scope="session", autouse=True)
def university_service_readiness():
    timeout = 180
    start_time = time.time()
    while time.time() < start_time + timeout:
        try:
            response = requests.get(UniversityService.SERVICE_URL + "/docs")
            response.raise_for_status()
        except requests.exceptions.ConnectionError:
            time.sleep(1)
        else:
            break
    else:
        raise RuntimeError(f"Auth service wasn't started during '{timeout}' seconds.' ")