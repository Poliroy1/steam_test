from pages.horizontal_slider_page import HorizontalSliderPage

url = "https://the-internet.herokuapp.com/horizontal_slider"

def test_horizontal_slider(browser):
    page = HorizontalSliderPage(browser)

    browser.get(url)
    page.wait_for_open()

    target_value = page.set_random_slider_value()

    current_value = page.get_correct_value()

    assert current_value == target_value, f"Ожидалось значение {target_value}, но отображается {current_value}"
