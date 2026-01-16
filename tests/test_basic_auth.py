import pytest
from pages.basic_auth_page import BasicAuthPage

URL = "https://the-internet.herokuapp.com/basic_auth"


@pytest.mark.parametrize(
    "username, password",
    [
        ('admin', 'admin'),
    ]
)
def test_basic_auth(browser, username, password):
    page = BasicAuthPage(browser)
    browser.open(URL, username, password)
    page.wait_for_open()

    actual_message = page.get_success_text()
    expected_message = "Congratulations! You must have the proper credentials."

    assert expected_message in actual_message, (f"Ожидали получить текст после логина: {expected_message},"
                                                f"Получили: {actual_message}")
