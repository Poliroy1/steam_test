from pages.alerts_context_click_page import AlertsContextClickPage

URL = 'https://the-internet.herokuapp.com/context_menu'


def test_alerts_context_click(browser):
    page = AlertsContextClickPage(browser)

    browser.get(URL)
    page.wait_for_open()

    page.click_right_button()

    alert_text = page.browser.get_alert_text()

    expected = "You selected a context menu"

    assert expected == alert_text, (f"Context click: Ожидался текст {expected} в алерте. "
                                    f"Фактический текст: {alert_text}")

    page.browser.accept_alert()
