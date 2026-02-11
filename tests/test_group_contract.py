import pytest
import requests.status_codes
from faker import Faker

from services.university.helpers.group_helper import GroupHelper

faker = Faker()


class TestGroupContract:
    @pytest.mark.xfail(
        reason="Known issue: anonymous request returns 403 (Access denied) instead of 401 (Unauthorized)",
        strict=False,
    )
    def test_create_group_anonym(self, university_api_utils_anonym):
        group_helper = GroupHelper(api_utils=university_api_utils_anonym)
        response = group_helper.post_group({"name": faker.name()})

        assert response.status_code == requests.status_codes.codes.unauthorized, (
            f"Wrong status code. Actual: '{response.status_code}', but expected: "
            f"{requests.status_codes.codes.unauthorized}"
        )

    def test_create_group_admin(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        response = group_helper.post_group({"name": faker.name()})

        assert response.status_code == requests.codes.created, (
            f"Wrong status code. Actual: '{response.status_code}', but expected: "
            f"{requests.status_codes.codes.authorized}"
        )
