from pages.dynamic_content_page import DynamicPage

URL = "https://the-internet.herokuapp.com/dynamic_content"
count_refresh = 100


def test_dynamic_content(browser):
    page = DynamicPage(browser)

    browser.get(URL)
    page.wait_for_open()

    duplicates = page.get_duplicate_image_src(count_refresh)

    assert len(duplicates) > len(
        set(duplicates)), f"Ожидалось хотя бы два одинаковых изображения, но получили: {duplicates}"
