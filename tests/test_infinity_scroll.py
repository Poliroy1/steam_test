from pages.Infinity_scroll_page import InfinityScrollPage

url = "https://the-internet.herokuapp.com/infinite_scroll"
my_age = 23


def test_infinite_scroll_paragraphs(browser):
    page = InfinityScrollPage(browser)

    browser.get(url)
    page.wait_for_open()

    count_paragraphs = page.get_paragraph(my_age)

    assert len(count_paragraphs) == my_age, f"Expected :{my_age} not in {count_paragraphs}"
