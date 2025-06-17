import allure
import logging

@allure.epic("Страница Russian Interest")
@allure.feature("Элементы страницы Russian Interest")
@allure.story("Проверка наличия элементов на странице Russian Interest")
def test_book_onegin(russian_interest_page):
    try:
        with allure.step("Проверка наличия книги Eugene Oneguine [Onegin]"):
            assert russian_interest_page.check_book_onegin(), (
                "На странице не найдена книга Eugene Oneguine [Onegin]"
            )
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            russian_interest_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        raise AssertionError(str(e))

@allure.feature("Сортировка книг")
@allure.story("Проверка сортировки по алфавиту")
def test_sort_books_alphabetically(russian_interest_page):

    with allure.step("Клик по кнопке сортировки по алфавиту"):
        russian_interest_page.sort_by_title()

    with allure.step("Проверка порядка книг после сортировки"):
        book_titles = russian_interest_page.get_book_titles()

        # Ищем индексы книг
        try:
            index_aatelisrosvo = book_titles.index("Aatelisrosvo Dubrovskij (Finnish)")
            index_annouchka = book_titles.index("Annouchka: A Tale")
        except ValueError as e:
            raise AssertionError(f"Не найдена книга: {str(e)}")

        # Проверяем, что Aatelisrosvo идет раньше Annouchka
        assert index_aatelisrosvo < index_annouchka, (
            f"Книга 'Aatelisrosvo Dubrovskij (Finnish)' ({index_aatelisrosvo}) "
            f"не идёт раньше книги 'Annouchka: A Tale' ({index_annouchka})"
        )