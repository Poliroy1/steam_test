from pages.dynamic_content_page import DynamicPage


def test_dynamic_content(browser):
    page = DynamicPage(browser)

    browser.get('http://theinternet.herokuapp.com/dynamic_content')
    page.wait_for_open()

    page.get_duplicate_image_src()

    duplicates = page.get_duplicate_image_src()

    assert len(duplicates) > len(set(duplicates)), f"Ожидалось хотя бы два одинаковых изображения, но получили: {duplicates}"