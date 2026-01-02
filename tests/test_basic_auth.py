from pages.basic_auth_page import BasicAuth


def test_basic_auth(browser):
    page = BasicAuth(browser)

    page.login("the-internet.herokuapp.com/basic_auth", "admin", "admin")

    page.wait_for_open()

    is_logged = page.is_logged_in()

    assert is_logged, f"Basic Auth: Ожидалась успешная авторизация (True). " \
        f"Фактический результат: {is_logged}"
