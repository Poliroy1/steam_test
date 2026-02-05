import random
import requests

from services.university.models.base_grade import BaseGrade
from services.university.models.grade_static_response import GradeStatisticResponse
from services.university.university_service import UniversityService
from services.university.helpers.grade_helper import GradeHelper
from services.university.models.grade_request import GradeRequest


class TestGradeStatsHighLevel:
    def test_stats_min_max_avg_calculated_correctly(
            self,
            university_api_utils_admin,
            create_student,
            create_teacher,
    ):
        service = UniversityService(api_utils=university_api_utils_admin)

        values = [
            BaseGrade.MIN_GRADE,
            BaseGrade.MIN_GRADE + 1,
            BaseGrade.MAX_GRADE
        ]

        for v in values:
            service.create_grade(GradeRequest(
                teacher_id=create_teacher.id,
                student_id=create_student.id,
                grade=v
            ))

        resp = GradeHelper(api_utils=university_api_utils_admin).get_grade_stats(
            student_id=create_student.id,
            teacher_id=create_teacher.id,
            group_id=create_student.group_id
        )

        assert resp.status_code == requests.status_codes.codes.ok, (
            f"Wrong status code. Actual: '{resp.status_code}', "
            f"Expected: '{requests.status_codes.codes.ok}'"
        )

        stats = GradeStatisticResponse.model_validate(resp.json())

        assert stats.count == len(values), (
            f"Wrong count. Actual: '{stats.count}', "
            f"Expected: '{len(values)}'"
        )

        assert stats.min == min(values), (
            f"Wrong min grade. Actual: '{stats.min}', "
            f"Expected: '{min(values)}'"
        )

        assert stats.max == max(values), (
            f"Wrong max grade. Actual: '{stats.max}', "
            f"Expected: '{max(values)}'"
        )

        expected_avg = sum(values) / len(values)
        assert stats.avg == expected_avg, (
            f"Wrong avg grade. Actual: '{stats.avg}', "
            f"Expected: '{expected_avg}'"
        )