from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class CategoriesPage(BasePage):
    R_CATEGORY = (By.XPATH, "/html/body/div[1]/div/div/ul[15]/li[4]/a")

    def is_r_category_present(self):
        self.log_action("Проверка наличия категории Russian Interest")
        try:
            self.wait_for_element_present(self.R_CATEGORY)
            self.log_action("Категория Russian Interest найдена")
            return True
        except TimeoutException:
            self.log_action("Категория Russian Interest не найдена")
            return False
