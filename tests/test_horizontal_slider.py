import pytest
from pages.horizontal_slider_page import HorizontalSliderPage


def test_horizontal_slider(browser):
    page = HorizontalSliderPage(browser)

    browser.get('https://the-internet.herokuapp.com/horizontal_slider')

    page.wait_for_open()

    target_value = page.set_random_slider_value()

    current_value = page.get_correct_value()

    assert current_value == target_value, f"Ожидалось значение {target_value}, но отображается {current_value}"
