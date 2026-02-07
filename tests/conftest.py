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
def group_factory(university_service):
    def _create(name: str | None = None):
        base = (name or faker.word()).strip()
        unique_name = f"{base}_{uuid4().hex[:8]}"

        req = GroupRequest(name=unique_name)
        return university_service.create_group(req)

    return _create


@pytest.fixture
def student_factory(university_service):
    def _create(group_id: int, **overrides):
        req = StudentRequest(
            first_name=overrides.get("first_name", faker.first_name()),
            last_name=overrides.get("last_name", faker.last_name()),
            degree=overrides.get("degree", random.choice([o for o in DegreeEnum])),
            phone=overrides.get("phone", faker.numerify("+7##########")),
            email=overrides.get("email", faker.email()),
            group_id=group_id,
        )
        return university_service.create_student(req)
    return _create


@pytest.fixture
def teacher_factory(university_service):
    def _create(**overrides):
        req = TeacherRequest(
            first_name=overrides.get("first_name", faker.first_name()),
            last_name=overrides.get("last_name", faker.last_name()),
            subject=overrides.get("subject", random.choice([o for o in SubjectEnum])),
        )
        return university_service.create_teacher(req)
    return _create


@pytest.fixture
def grade_factory(university_service):
    def _create(teacher_id: int, student_id: int, grade: int | None = None):
        if grade is None:
            grade = random.randint(MIN_GRADE, MAX_GRADE)

        req = GradeRequest(teacher_id=teacher_id, student_id=student_id, grade=grade)
        return university_service.create_grade(req)

    return _create

