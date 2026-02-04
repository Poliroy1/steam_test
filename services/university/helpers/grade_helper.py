import requests
from services.general.helpers.base_helper import BaseHelper


class GradeHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"
    ENDPOINT_STATS = f"{ENDPOINT_PREFIX}/stats/"

    def post_grade(self, data: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, data=data)
        return response

    def get_grade(self, student_id: int, teacher_id: int, group_id: int) -> requests.Response:
        params = {
            "student_id": student_id,
            "teacher_id": teacher_id,
            "group_id": group_id,
        }
        return self.api_utils.get(self.ROOT_ENDPOINT, params=params)

    def get_grade_stats(self, student_id: int, teacher_id: int, group_id: int) -> requests.Response:
        params = {
            "student_id": student_id,
            "teacher_id": teacher_id,
            "group_id": group_id,
        }
        response = self.api_utils.get(self.ENDPOINT_STATS, params=params)
        return response
