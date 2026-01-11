from pages.alerts_page import AlertsPage
from faker import Faker

faker = Faker()

url = "https://the-internet.herokuapp.com/javascript_alerts"

def test_javascript_alerts_full_scenario(browser):
    page = AlertsPage(browser)

    browser.get(url)
    page.wait_for_open()

    page.click_js_alert()

    alert_text = page.get_alert_text()
    assert "I am a JS Alert" in alert_text, f"JS Alert: ожидался текст 'I am a JS Alert' в алерте.фактический текст алерта: '{alert_text}'"

    page.accept_alert()

    result = page.text_results.get_text()

    assert "You successfully clicked an alert" == result, f"JS Alert: ожидался результат 'You successfully clicked an alert'. фактический результат: '{result}'"

    page.click_js_confirm()

    alert_text = page.get_alert_text()
    assert "I am a JS Confirm" in alert_text, f"JS Confirm: ожидался текст 'I am a JS Confirm' в алерте. фактический текст алерта: '{alert_text}'"

    page.accept_alert()

    result = page.text_results.get_text()
    assert "You clicked: Ok" == result, f"JS Confirm: ожидался результат 'You clicked: Ok'. фактический результат: '{result}'"

    page.click_js_prompt()

    alert_text = page.get_alert_text()
    assert "I am a JS prompt" in alert_text, f"JS prompt: ожидался текст 'I am a JS prompt' в алерте. фактический текст алерта: '{alert_text}'"

    random_text = faker.word()
    page.browser.send_keys_alert(random_text)

    page.accept_alert()

    result = page.text_results.get_text()
    expected = f"You entered: {random_text}"

    assert expected == result, f"JS Prompt: ожидался результат '{expected}'. фактический результат: '{result}'"
