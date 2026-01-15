from pages.iframe_page import IframePage

URL = "https://demoqa.com/frames"
TEXT_NESTED_FRAMES = "Nested Frames".strip().lower()
TEXT_FRAMES = "Frames".strip().lower()


def test_iframe(browser):
    page = IframePage(browser)

    browser.get(URL)
    page.wait_for_open()

    page.click_alerts_menu()
    page.click_nested()
    page.wait_for_open()

    actual_rs = page.get_unique_text_nested_frames()
    expected_rs = TEXT_NESTED_FRAMES
    assert actual_rs == expected_rs, f" Nested text: ожидался текст {expected_rs}, фактический — '{actual_rs}'"

    actual_rs = page.get_child_text()
    expected_rs = 'Child Iframe'
    assert expected_rs == actual_rs, f"Child iframe: ожидался текст {expected_rs}, фактический — '{actual_rs}'"

    actual_rs = page.get_parent_text()
    expected_rs = 'Parent frame'
    assert expected_rs == actual_rs, f"Parent iframe: ожидался текст {expected_rs},фактический — '{actual_rs}'"

    page.click_frames()
    page.wait_for_open()

    actual_rs = page.get_unique_text_frames()
    expected_rs = TEXT_FRAMES
    assert actual_rs == expected_rs, f" Frames text: ожидался текст {expected_rs}, фактический — '{actual_rs}'"

    up_iframe = page.get_text_to_up_iframe()
    down_iframe = page.get_text_to_down_iframe()

    assert up_iframe == down_iframe, f"Frames: тексты совпадают. Верхний — '{up_iframe}', нижний — '{down_iframe}'"
