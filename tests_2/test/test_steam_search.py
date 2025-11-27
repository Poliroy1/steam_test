import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

URLS = {
    "en": "https://store.steampowered.com/?l=english",
    "ru": "https://store.steampowered.com/?l=russian"
}

@pytest.mark.parametrize("lang", ["en", "ru"])
@pytest.mark.parametrize("game,n", [("The Witcher", 10), ("Fallout", 20)])
def test_steam_search(driver, lang, game, n):
    home = HomePage(driver)
    results = SearchResultsPage(driver)

    home.open(URLS[lang])
    home.search_game(game)
    results.apply_price_filter()
    prices = results.get_prices(n)

    assert prices == sorted(prices, reverse=True)