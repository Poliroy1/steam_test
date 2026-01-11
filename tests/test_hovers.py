from pages.hovers_page import HoversPage

url = "https://the-internet.herokuapp.com/hovers"

def test_hovers(browser):

    page = HoversPage(browser)

    browser.get(url)
    page.wait_for_open()

    users_count = page.avatars.count()

    for index in range(users_count):

        page.hover_and_click_profile(index)

        assert f"users/{index + 1}" in browser.get_current_url()

        browser.go_back()
        page.wait_for_open()


