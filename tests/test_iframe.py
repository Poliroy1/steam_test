from pages.iframe_page import IframePage

url = "https://demoqa.com/frames"

def test_iframe(browser):
    page = IframePage(browser)

    browser.get(url)
    page.wait_for_open()

    page.click_nested()

    assert 'Child Iframe' == page.get_child_text()
    assert 'Parent frame' == page.get_parent_text()

    page.click_frames()
    page.wait_for_open()

    up_iframe = page.get_text_to_up_iframe()
    down_iframe = page.get_text_to_down_iframe()

    assert up_iframe == down_iframe
    
