from pages.handlers_page import HandlersPage

url = "https://the-internet.herokuapp.com/windows"


def test_handlers(browser):
    page = HandlersPage(browser)

    browser.get(url)
    page.wait_for_open()

    main_handle = browser.get_current_window_handle()

    handles_before = set(browser.get_window_handles())
    page.click_link()

    handles_after = set(browser.get_window_handles())
    first_new_handle = (handles_after - handles_before).pop()

    browser.switch_to_window_by_handle(first_new_handle)
    assert page.get_header_text() == "New Window"

    browser.switch_to_window_by_handle(main_handle)
    page.wait_for_open()

    handles_before = set(browser.get_window_handles())
    page.click_link()

    handles_after = set(browser.get_window_handles())
    second_new_handle = (handles_after - handles_before).pop()

    browser.switch_to_window_by_handle(second_new_handle)
    assert page.get_header_text() == "New Window"

    browser.switch_to_window_by_handle(main_handle)
    page.wait_for_open()

    browser.switch_to_window_by_handle(first_new_handle)
    browser.close()

    browser.switch_to_window_by_handle(second_new_handle)
    browser.close()