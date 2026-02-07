from services.university.helpers.student_helper import StudentHelper


class TestDeleteStudent:
    def test_delete_student_success(self, university_api_utils_admin, create_student):
        student_helper = StudentHelper(api_utils=university_api_utils_admin)
        response = student_helper.delete_student(create_student.id)
        assert response.status_code == 200, (f"Wrong status code. Actual: '{response.status_code}',"
                                             f" Expected: '200'")