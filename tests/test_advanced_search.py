import allure
import logging

import pytest


@allure.epic("Расширенный поиск")
@allure.feature("Поиск книги")
@allure.story("Поиск 'Евгения Онегина'")
@pytest.mark.parametrize(
    "author, title, subject",
    [("Pushkin", "Eugene Oneguine [Onegin]", "Novels in verse")],
)
def test_advanced_search(advancedsearch_page, author, title, subject):
    try:
        with allure.step("Заполнение формы поиска"):
            advancedsearch_page.fill_advanced_search_book(author, title, subject)

        with allure.step("Клик на кнопку поиска"):
            advancedsearch_page.search_btn_click()

        with allure.step("Проверка ID найденной книги"):
            try:
                with allure.step("Проверка наличия найденной книги"):
                    assert (
                        advancedsearch_page.is_search_book_present()
                    ), "На странице не найдена книга"
            except AssertionError as e:
                logging.error(f"Ошибка в тесте: {str(e)}")
                allure.attach(
                    advancedsearch_page.browser.get_screenshot_as_png(),
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG,
                )
                raise AssertionError(str(e))

    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {e}")

        allure.attach(
            advancedsearch_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )

        raise AssertionError(str(e))
