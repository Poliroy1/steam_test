import requests
from faker import Faker

from services.university.helpers.student_helper import StudentHelper

faker = Faker()


class TestStudentContract:
    def test_create_student_anonym(self, university_api_utils_anonym, student_payload):
        student_helper = StudentHelper(api_utils=university_api_utils_anonym)

        response = student_helper.post_student(json=student_payload.model_dump())

        assert response.status_code == requests.codes.unauthorized, (
            f"Wrong status code. Actual: '{response.status_code}', but expected: {requests.codes.authorized}"
        )
