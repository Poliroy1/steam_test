from pages.handlers_page import HandlersPage

URL = "https://the-internet.herokuapp.com/windows"


def test_handlers(browser):
    page = HandlersPage(browser)

    browser.get(URL)
    page.wait_for_open()

    main_handle = browser.get_current_window_handle()

    handles_before = set(browser.get_window_handles())
    page.click_link()

    handles_after = set(browser.get_window_handles())
    first_new_handle = (handles_after - handles_before).pop()

    browser.switch_to_window_by_handle(first_new_handle)
    actual_rs = page.get_header_text()
    expected_rs = "New Window"

    assert actual_rs == expected_rs, f"Новое окно: ожидался заголовок '{expected_rs}', фактический — '{actual_rs}'"

    browser.switch_to_window_by_handle(main_handle)
    page.wait_for_open()

    handles_before = set(browser.get_window_handles())
    page.click_link()

    handles_after = set(browser.get_window_handles())
    second_new_handle = (handles_after - handles_before).pop()

    browser.switch_to_window_by_handle(second_new_handle)
    actual_rs = page.get_header_text()
    expected_rs = "New Window"

    assert actual_rs == expected_rs, f"Второе окно: ожидался заголовок '{expected_rs}', фактический — '{actual_rs}'"

    browser.switch_to_window_by_handle(main_handle)
    page.wait_for_open()

    browser.switch_to_window_by_handle(first_new_handle)
    browser.close()

    browser.switch_to_window_by_handle(second_new_handle)
    browser.close()
