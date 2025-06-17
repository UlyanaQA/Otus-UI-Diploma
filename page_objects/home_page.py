
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage

class HomePage(BasePage):
    SEARCH_SUBMIT = (By.XPATH, '//button[@type="submit"]')
    SEARCH_INPUT = (By.CLASS_NAME, "search-input")
    SEARCH_RESULTS = (By.CLASS_NAME, "booklink")
    BOOK_TITLE = (By.CSS_SELECTOR, "span.title:contains('The Adventures of Sherlock Holmes')")
    NO_RESULTS_MESSAGE = (By.XPATH, "//*[contains(text(), 'No results found')]")

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

    def no_results_found(self):
        try:
            return WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located(self.NO_RESULTS_MESSAGE))
        except TimeoutException:
            return True