import allure
import logging


@allure.epic("Страница категорий")
@allure.feature("Элементы страницы категорий")
@allure.story("Проверка наличия категории Russian Interest")
def test_russian_interest(categories_page):
    try:
        with allure.step("Проверка наличия категории Russian Interest"):
            assert (
                categories_page.is_r_category_present()
            ), "На странице не найдена категория Russian Interest"
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            categories_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        raise AssertionError(str(e))
