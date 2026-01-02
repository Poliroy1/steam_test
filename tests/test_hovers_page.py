from pages.hovers_page import HoversPage

def test_hovers(browser):
    # Открываем страницу
    page = HoversPage(browser)
    browser.get("https://the-internet.herokuapp.com/hovers")
    page.unique_element.wait_for_presence()  # ждём, что страница загрузилась

    # Перебираем все аватары
    for index, avatar in enumerate(page.avatars, start=1):
        # Наведение на аватар + ожидание имени
        user_name = page.hover_and_get_user_name(index)

        # Проверка имени пользователя
        assert f"user{index}" in user_name, f"Имя пользователя {index} не соответствует"

        # Клик по ссылке профиля
        page.click_profile_link(index)

        # Проверка URL
        assert f"/users/{index}" in browser.driver.current_url, f"URL профиля {index} некорректен"

        # Возврат на страницу с аватарами
        browser.driver.back()