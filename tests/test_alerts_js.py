from pages.alerts_js_page import AlertsJSPage
from faker import Faker

faker = Faker()

url = "https://the-internet.herokuapp.com/javascript_alerts"

def test_javascript_alerts_full_scenario(browser):
    page = AlertsJSPage(browser)

    browser.get(url)
    page.wait_for_open()

    page.js_click_js_alert()

    alert_text = page.browser.get_alert_text()
    assert "I am a JS Alert" in alert_text, f"JS Alert: Ожидался текст 'I am a JS Alert' в алерте.Фактический текст алерта: '{alert_text}'"

    page.browser.accept_alert()

    result = page.text_results.get_text()

    assert "You successfully clicked an alert" == result, f"JS Alert: Ожидался результат 'You successfully clicked an alert'. Фактический результат: '{result}'"

    page.js_click_js_confirm()

    alert_text = page.browser.get_alert_text()
    assert "I am a JS Confirm" in alert_text, f"JS Confirm: Ожидался текст 'I am a JS Confirm' в алерте. Фактический текст алерта: '{alert_text}'"

    page.browser.accept_alert()

    result = page.text_results.get_text()
    assert "You clicked: Ok" == result, f"JS Confirm: Ожидался результат 'You clicked: Ok'. Фактический результат: '{result}'"

    page.js_click_js_prompt()

    alert_text = page.browser.get_alert_text()
    assert "I am a JS prompt" in alert_text, f"JS Prompt: Ожидался текст 'I am a JS prompt' в алерте. Фактический текст алерта: '{alert_text}'"

    random_text = faker.word()
    page.browser.send_keys_alert(random_text)

    page.browser.accept_alert()

    result = page.text_results.get_text()
    expected = f"You entered: {random_text}"

    assert expected == result, f"JS Prompt: Ожидался результат '{expected}'. Фактический результат: '{result}'"
