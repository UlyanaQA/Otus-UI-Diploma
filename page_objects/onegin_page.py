from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class OneginPage(BasePage):
    BOOK_TITLE = (By.XPATH, '//*[@id="book_title"]')
    DOWNLOAD_BTN = (By.XPATH, '//*[@id="download_options_table"]/tbody/tr[3]/td[2]')
    READ_MORE_BTN = (By.XPATH, '//*[@id="read_more"]')
    SHOW_LESS_BTN = (By.XPATH, '//*[@id="download"]/div[1]/span/label[2]')

    def is_onegin_title_present(self):
        self.log_action("Проверка наличия названия книги")
        try:
            self.wait_for_element_present(self.BOOK_TITLE)
            self.log_action("Название книги найдено")
            return True
        except TimeoutException:
            self.log_action("Название книги не найдено")
            return False

    def is_download_btn_present(self):
        self.log_action("Проверка наличия кнопки сохранения книги")
        try:
            self.wait_for_element_present(self.DOWNLOAD_BTN)
            self.log_action("Кнопка сохранения книги найдена")
            return True
        except TimeoutException:
            self.log_action("Кнопка сохранения книги не найдена")
            return False

    def read_more_click(self):
        self.browser.find_element(*self.READ_MORE_BTN).click()
        return self

    def is_show_less_btn_present(self):
        self.log_action("Проверка наличия кнопки сокрытия информации о книге")
        try:
            self.wait_for_element_present(self.DOWNLOAD_BTN)
            self.log_action("Кнопка сокрытия информации о книге найдена")
            return True
        except TimeoutException:
            self.log_action("Кнопка сокрытия информации о книге не найдена")
            return False
