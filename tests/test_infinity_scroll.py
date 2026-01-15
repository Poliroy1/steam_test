from pages.Infinity_scroll_page import InfinityScrollPage

URL = "https://the-internet.herokuapp.com/infinite_scroll"
MY_AGE = 23


def test_infinite_scroll_paragraphs(browser):
    page = InfinityScrollPage(browser)

    browser.get(URL)
    page.wait_for_open()

    count_paragraphs = page.get_paragraph(MY_AGE)

    assert len(count_paragraphs) == MY_AGE, f"Expected :{MY_AGE} not in {count_paragraphs}"
