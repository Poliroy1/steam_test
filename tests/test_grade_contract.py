import random
from faker import Faker

from services.university.helpers.grade_helper import GradeHelper
from services.university.models.grade_request import GradeRequest


faker = Faker()
GRADE = random.randint(GradeRequest.MIN_GRADE, GradeRequest.MAX_GRADE)

class TestGrade:
    def test_create_grade_contract(self, university_api_utils_admin, create_student, create_teacher):
        grade_helper = GradeHelper(api_utils=university_api_utils_admin)
        grade = grade_helper.post_grade(
            {'teacher_id': create_teacher.id, 'student_id': create_student.id, 'grade': GRADE})
        assert grade.status_code == 201,\
            (f'Actual status code: {grade.status_code},'
            f' But expected code{grade.status_code}')


