from services.university.helpers.student_helper import StudentHelper


class TestDeleteContract:
    def test_delete_contract(self, university_api_utils_admin, create_student):
        student_helper = StudentHelper(api_utils=university_api_utils_admin)
        response = student_helper.delete_student(create_student.id)
        assert response.status_code == 200, (f'Excepted Status Code: {response.status_code},'
                                             f'Actual Status Code: {response.status_code} ')