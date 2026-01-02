from pages.alerts_context_click import AlertsContextClick

def test_alerts_context_click(browser):
    page = AlertsContextClick(browser)

    browser.get('https://the-internet.herokuapp.com/context_menu')
    page.wait_for_open()

    page.click_right_button()

    alert_text = page.get_alert_text()

    expected = "You selected a context menu"

    assert expected == alert_text, f"Context click: Ожидался текст {expected} в алерте. Фактический текст: {alert_text}"

    page.accept_alert()


