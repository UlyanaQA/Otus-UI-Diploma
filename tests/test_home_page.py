import allure
import logging


@allure.epic("Домашняя страница")
@allure.feature("Элементы домашней страницы")
@allure.story("Проверка наличия поисковой строки")
def test_search_button(home_page):
    try:
        with allure.step("Проверка наличия поисковой строки"):
            assert (
                home_page.is_search_btn_present()
            ), "На странице не найдена поисковая строка"
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            home_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        raise AssertionError(str(e))


@allure.epic("Домашняя страница")
@allure.feature("Элементы домашней страницы")
@allure.story("Проверка наличия топа последних книг")
def test_top_books(home_page):
    try:
        with allure.step("Проверка наличия топа последних книг"):
            assert (
                home_page.is_top_books_present()
            ), "На странице не найден топ последних книг"
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            home_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        raise AssertionError(str(e))
