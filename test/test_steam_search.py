import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from utils.config_reader import ConfigReader

cfg = ConfigReader()

@pytest.mark.parametrize("lang", cfg.languages)
@pytest.mark.parametrize("game,n", [("The Witcher", 10), ("Fallout", 20)])
def test_steam_search(driver, lang, game, n):
    home = HomePage(driver)
    results = SearchResultsPage(driver)

    url = cfg.url_for_lang(lang)
    driver.get(url)
    home.wait_for_open()

    home.search_game(game)
    results.apply_price_filter()
    actual_result = results.get_prices(n)

    expected = sorted(actual_result, reverse=True)

    assert actual_result == expected, f'Цены отсортированы неверно. Ожидалось {expected}, получили {actual_result}'