from pages.alerts_page import AlertsPage
from faker import Faker

faker = Faker()

URL = "https://the-internet.herokuapp.com/javascript_alerts"


def test_javascript_alerts_full_scenario(browser):
    page = AlertsPage(browser)

    browser.get(URL)
    page.wait_for_open()

    page.click_js_alert()

    actual_result = page.browser.get_alert_text()
    expected_result = "I am a JS Alert"

    assert actual_result == expected_result, f"JS Alert: ожидался текст {expected_result} в алерте. Фактический текст алерта: '{actual_result}'"

    page.browser.accept_alert()

    actual_result = page.text_results.get_text()
    expected_result = "You successfully clicked an alert"

    assert actual_result == expected_result, f"JS Alert: ожидался результат {expected_result}. Фактический результат: '{actual_result}'"

    page.click_js_confirm()

    actual_result = page.browser.get_alert_text()
    expected_result = "I am a JS Confirm"

    assert actual_result == expected_result, f"JS Confirm: ожидался текст {expected_result} в алерте. Фактический текст алерта: '{actual_result}'"

    page.browser.accept_alert()

    actual_result = page.text_results.get_text()
    expected_result = "You clicked: Ok"

    assert actual_result == expected_result, f"JS Confirm: ожидался результат {expected_result}. Фактический результат: '{actual_result}'"

    page.click_js_prompt()

    actual_result = page.browser.get_alert_text()
    expected_result = "I am a JS prompt"

    assert actual_result in expected_result, f"JS prompt: ожидался текст expected_result в алерте. Фактический текст алерта: '{actual_result}'"

    random_text = faker.word()
    page.browser.send_keys_alert(random_text)

    page.browser.accept_alert()

    actual_result = page.text_results.get_text()
    expected_result = f"You entered: {random_text}"

    assert actual_result == expected_result, f"JS Prompt: ожидался результат '{expected_result}'. Фактический результат: '{actual_result}'"
