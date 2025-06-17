from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage

class RussianInterestPage(BasePage):
    BOOK_TITLE = (By.XPATH, "//span[@class='title' and contains(text(), 'Eugene Oneguine [Onegin]')]")
    SORT_BY_TITLE = (By.XPATH, '//*[@id="content"]/div[2]/div/ul/li[1]/a/span[2]/span')

    def check_book_onegin(self):
        book_title_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.BOOK_TITLE)
        )
        return book_title_element.text.strip() == "Eugene Oneguine [Onegin]"

    def sort_by_title(self):
        self.browser.find_element(*self.SORT_BY_TITLE).click()
        return self

    def get_book_titles(self):
        """Возвращает список названий книг на странице."""
        book_elements = self.browser.find_elements(By.CSS_SELECTOR, ".booklink .title")
        return [book.text for book in book_elements]

