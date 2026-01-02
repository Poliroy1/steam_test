from pages.Infinity_scroll_page import InfinityScrollPage


def test_infinite_scroll_paragraphs(browser):
    expected_paragraphs = 23

    page = InfinityScrollPage(browser)

    browser.get('https://the-internet.herokuapp.com/infinite_scroll')
    page.wait_for_open()

    page.scroll_until_paragraph_count(expected_paragraphs)

    actual_count = page.get_paragraph_count()

    assert actual_count == expected_paragraphs, f"Expected {expected_paragraphs} paragraphs, but found {actual_count}"