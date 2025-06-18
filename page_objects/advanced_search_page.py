from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AdvancedSearchPage(BasePage):
    AUTHOR_FIELD = (By.XPATH, '//*[@id="author"]')
    TITLE_FIELD = (By.XPATH, '//*[@id="title"]')
    SUBJECT_FIELD = (By.XPATH, '//*[@id="subject"]')
    ID_BOOK = (By.XPATH, '//*[@id="content"]/table/tbody/tr[2]/td[1]')
    SEARCH_BTN = (By.XPATH, '//*[@id="submit"]')

    def fill_advanced_search_book(self, author, title, subject):
        self.log_action(f"Поиск книги: {title}")
        self.fill_field(self.AUTHOR_FIELD, author)
        self.fill_field(self.TITLE_FIELD, title)
        self.fill_field(self.SUBJECT_FIELD, subject)

    def search_btn_click(self):
        self.browser.find_element(*self.SEARCH_BTN).click()
        return self

    def is_search_book_present(self):
        self.log_action("Проверка наличия найденной книги")
        try:
            self.wait_for_element_present(self.ID_BOOK)
            self.log_action("Книга найдена")
            return True
        except TimeoutException:
            self.log_action("Книга не найдена")
            return False
