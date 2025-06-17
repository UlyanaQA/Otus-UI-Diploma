import allure
import logging

@allure.epic("Страница книги")
@allure.feature("Элементы страницы книги")
@allure.story("Проверка наличия названия книги")
def test_title_book(onegin_page):
    try:
        with allure.step("Проверка наличия названия книги"):
            assert onegin_page.is_onegin_title_present(), (
                "На странице не найдено название книги"
            )
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            onegin_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        raise AssertionError(str(e))

@allure.epic("Страница книги")
@allure.feature("Элементы страницы книги")
@allure.story("Проверка наличия кнопки сохранения книги")
def test_download_button(onegin_page):
    try:
        with allure.step("Проверка наличия кнопки сохранения книги"):
            assert onegin_page.is_download_btn_present(), (
                "На странице не найдена кнопка сохранения книги"
            )
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            onegin_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        raise AssertionError(str(e))

@allure.epic("Страница книги")
@allure.feature("Элементы страницы книги")
@allure.story("Проверка разворачивания информации о книге")
def test_show_info(onegin_page):
    with allure.step("Клик по кнопке 'Read more'"):
        onegin_page.read_more_click()

    with allure.step("Проверка появления кнопки 'Show less'"):
        assert onegin_page.is_show_less_btn_present(), "Кнопка 'Show less' не появилась после нажатия 'Read more'"


