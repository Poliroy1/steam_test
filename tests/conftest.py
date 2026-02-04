import random
import time
import pytest
import requests
from services.auth.auth_service import AuthService
from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest
from services.university.models.base_student import DegreeEnum
from services.university.models.base_teacher import SubjectEnum
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService
from utils.api_utils import ApiUtils
from faker import Faker


faker = Faker()
GROUP_ID = 1

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
def create_student(university_api_utils_admin):
    university_service = UniversityService(api_utils=university_api_utils_admin)
    student = StudentRequest(first_name=faker.first_name(),
                             last_name=faker.last_name(),
                             degree=random.choice([option for option in DegreeEnum]),
                             phone=faker.numerify('+7##########'),
                             email=faker.email(), group_id=GROUP_ID)
    student_response = university_service.create_student(student)
    return student_response

@pytest.fixture(scope="function", autouse=False)
def create_group(university_api_utils_admin):
    university_service = UniversityService(university_api_utils_admin)
    group = GroupRequest(name=faker.name())
    group_response = university_service.create_group(group)
    return group_response

@pytest.fixture(scope="function", autouse=False)
def create_teacher(university_api_utils_admin):
    university_service = UniversityService(api_utils=university_api_utils_admin)
    teacher = TeacherRequest(first_name=faker.first_name(), last_name=faker.last_name(),
                             subject=random.choice([option for option in SubjectEnum]), )
    teacher_response = university_service.create_teacher(teacher)
    return teacher_response

@pytest.fixture
def student_payload():
    return StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        degree=random.choice([d for d in DegreeEnum]),
        phone=faker.numerify("+7##########"),
        email=faker.email(),
        group_id=GROUP_ID
    ).model_dump()
