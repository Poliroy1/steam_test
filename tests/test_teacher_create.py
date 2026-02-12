import random

from faker import Faker

from logger.logger import Logger
from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.base_teacher import SubjectEnum

faker = Faker()


class TestTeacher:
    def test_teacher_create(self, university_api_utils_admin):
        Logger.info("### Step 1. Create teacher")
        teacher_helper = TeacherHelper(api_utils=university_api_utils_admin)
        response = teacher_helper.post_teacher(
            {
                "first_name": faker.first_name(),
                "last_name": faker.last_name(),
                "subject": random.choice([option for option in SubjectEnum]),
            }
        )
        assert response.status_code == 201, (
            f"but Excepted : {response.status_code} Wrong response  status Code Actual: {response.status_code} "
        )
