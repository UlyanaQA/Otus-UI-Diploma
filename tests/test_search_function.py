import allure
import pytest


@pytest.mark.parametrize(
    "query, expected_result", [("Sherlock Holmes", True), ("RandomBook-12345", False)]
)
def test_search_books(home_page, base_url, query, expected_result):
    with allure.step(f"Поиск книги: '{query}'"):
        home_page.search_for(query)

    if expected_result:
        with allure.step("Проверка, что найдены книги"):
            assert home_page.results_contain(), f"Книги '{query}' не найдены"

        if query == "Sherlock Holmes":
            with allure.step("Проверка названия книги"):
                assert (
                    home_page.check_book_title()
                ), "Название книги 'The Adventures of Sherlock Holmes' не найдено"

    else:
        with allure.step("Проверка сообщения 'No results found'"):
            assert (
                home_page.no_results_found()
            ), "Сообщение об отсутствии результатов не отображается"
