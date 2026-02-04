import requests
from services.general.helpers.base_helper import BaseHelper


class StudentHelper(BaseHelper):
    ENDPOINT_PREFIX = "/students"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"

    def post_student(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def get_students(self) -> requests.Response:
        response = self.api_utils.get(self.ENDPOINT_PREFIX)
        return response

    def get_student(self, student_id: int) -> requests.Response:
        response = self.api_utils.get(f'{self.ROOT_ENDPOINT}{student_id}')
        return response

    def delete_student(self, student_id: int) -> requests.Response:
        response = self.api_utils.delete(f'{self.ROOT_ENDPOINT}{student_id}')
        return response
