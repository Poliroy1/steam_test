import random
import requests

from services.university.models.base_grade import BaseGrade
from services.university.university_service import UniversityService
from services.university.helpers.grade_helper import GradeHelper
from services.university.models.grade_request import GradeRequest


class TestGradingBusinessFlow:
    def test_teacher_sets_grade_to_student(self,
        university_api_utils_admin,
        create_group,
        create_student,
        create_teacher
    ):
        service = UniversityService(api_utils=university_api_utils_admin)

        student = create_student
        teacher = create_teacher

        grade_value = random.randint(
            BaseGrade.MIN_GRADE,
            BaseGrade.MAX_GRADE
        )

        created_grade = service.create_grade(GradeRequest(
            teacher_id=teacher.id,
            student_id=student.id,
            grade=grade_value
        ))

        stats_resp = GradeHelper(api_utils=university_api_utils_admin).get_grade_stats(
            student_id=student.id,
            teacher_id=teacher.id,
            group_id=student.group_id
        )

        stats = stats_resp.json()

        assert created_grade.grade == grade_value, \
            (f"Wrong grade value. Actual: '{created_grade.grade}', "
             f"Expected: '{grade_value}'")

        assert stats_resp.status_code == requests.status_codes.codes.ok, \
            (f"Wrong status code. Actual: '{stats_resp.status_code}', "
             f"Expected: '{requests.status_codes.codes.ok}'")

        assert stats["count"] == 1, \
            (f"Wrong count. Actual: '{stats['count']}', "
             f"Expected: '1'")

        assert stats["min"] == grade_value, \
            (f"Wrong min grade. Actual: '{stats['min']}', "
             f"Expected: '{grade_value}'")

        assert stats["max"] == grade_value, \
            (f"Wrong max grade. Actual: '{stats['max']}', "
             f"Expected: '{grade_value}'")

        assert stats["avg"] == grade_value, \
            (f"Wrong avg grade. Actual: '{stats['avg']}', "
             f"Expected: '{grade_value}'")