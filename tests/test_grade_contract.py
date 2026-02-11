import random

from faker import Faker
from services.university.models.base_grade import MAX_GRADE, MIN_GRADE
from services.university.helpers.grade_helper import GradeHelper
from services.university.models.grade_request import GradeRequest

faker = Faker()


class TestGrade:
    def test_create_grade_contract(self, university_api_utils_admin, create_student, create_teacher):
        grade_helper = GradeHelper(api_utils=university_api_utils_admin)
        grade_value = random.randint(MIN_GRADE, MAX_GRADE)

        grade = grade_helper.post_grade(
            {"teacher_id": create_teacher.id, "student_id": create_student.id, "grade": grade_value}
        )
        assert grade.status_code == 201, (
            f"Actual status code: {grade.status_code}, But expected code{grade.status_code}"
        )
