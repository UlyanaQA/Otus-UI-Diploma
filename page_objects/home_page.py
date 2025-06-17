from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage

class HomePage(BasePage):
    SEARCH_SUBMIT = (By.XPATH, '//button[@type="submit"]')
    SEARCH_INPUT = (By.CLASS_NAME, "search-input")
    SEARCH_RESULTS = (By.CLASS_NAME, "booklink")
    BOOK_TITLE = (By.XPATH, "//span[@class='title' and contains(text(), 'The Adventures of Sherlock Holmes')]")
    NO_RESULTS_MESSAGE = (By.XPATH, "//*[contains(text(), 'No results found')]")
    TOP_BOOKS = (By.XPATH, "/html/body/div[1]/div/div[1]")

    def is_search_btn_present(self):
        self.log_action("Проверка наличия строки поиска")
        try:
            self.wait_for_element_present(self.SEARCH_INPUT)
            self.log_action("Строка поиска найдена")
            return True
        except TimeoutException:
            self.log_action("Строка поиска не найдена")
            return False

    def is_top_books_present(self):
        self.log_action("Проверка наличия топа последних книг")
        try:
            self.wait_for_element_present(self.TOP_BOOKS)
            self.log_action("Топ последних книг найден")
            return True
        except TimeoutException:
            self.log_action("Топ последних книг не найден")
            return False

    def search_for(self, query):
        self.fill_field(self.SEARCH_INPUT, query)
        self.browser.find_element(*self.SEARCH_SUBMIT).click()
        return self

    def results_contain(self):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(self.SEARCH_RESULTS))
            return True
        except TimeoutException:
            return False

    def check_book_title(self):
        """Проверяет, что элемент с названием книги 'The Adventures of Sherlock Holmes' присутствует."""
        book_title_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.BOOK_TITLE)
        )
        return book_title_element.text.strip() == "The Adventures of Sherlock Holmes"

    def no_results_found(self):
        try:
            return WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located(self.NO_RESULTS_MESSAGE))
        except TimeoutException:
            return True