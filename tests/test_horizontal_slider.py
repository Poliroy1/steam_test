import random

from pages.horizontal_slider_page import HorizontalSliderPage

URL = "https://the-internet.herokuapp.com/horizontal_slider"


def test_horizontal_slider(browser):
    page = HorizontalSliderPage(browser)

    browser.get(URL)
    page.wait_for_open()

    min_v, max_v, step = page.get_slider_bounds()

    num_steps = int((max_v - min_v) / step) - 1

    rand_step = random.randrange(1, num_steps + 1)

    target_value = min_v + rand_step * step

    page.set_slider_value(target_value)

    current_value = page.get_current_value()

    assert current_value == target_value, (
        f"Ожидалось значение {target_value}, но отображается {current_value}"
    )
