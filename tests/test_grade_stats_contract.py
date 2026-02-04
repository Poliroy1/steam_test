import requests
from services.university.helpers.grade_helper import GradeHelper

class TestGradeStatsLowLevel:
    def test_get_stats_unauthorized(self, university_api_utils_anonym):
        grade_helper = GradeHelper(api_utils=university_api_utils_anonym)

        response = grade_helper.get_grade_stats(student_id=1, teacher_id=1, group_id=1)

        assert response.status_code == requests.codes.unauthorized, \
            f"Expected 401, got {response.status_code}"

    def test_get_stats_authorized(self, university_api_utils_admin):
        grade_helper = GradeHelper(api_utils=university_api_utils_admin)

        response = grade_helper.get_grade_stats(student_id=1, teacher_id=1, group_id=1)

        assert response.status_code == requests.codes.unauthorized, \
            f"Expected 401, got {response.status_code}, body: {response.text}"
