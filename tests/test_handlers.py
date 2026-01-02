from pages.handlers_page import HandlersPage


def test_handlers(browser):
    page = HandlersPage(browser)

    browser.get("https://the-internet.herokuapp.com/handlers")
    page.wait_for_open()

    page.click_link()

    assert 'New window' == page.get_header_text()

    assert 'New window' == page.get_title()

    browser.switch_to_default_window()
    page.wait_for_open()

    page.click_link()

    assert 'New window' == page.get_header_text()

    assert 'New window' == page.get_title()

    browser.switch_to_default_window()
    page.wait_for_open()

    browser.close()
    browser.switch_to_default_window()
    browser.close()




