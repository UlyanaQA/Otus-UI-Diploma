import logging
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def log_action(self, message):
        self.logger.info(message)

    def open(self, url):
        self.log_action(f"Открытие страницы: {url}")
        self.browser.get(url)

    def wait_for_element_present(self, locator, timeout=3):
        self.log_action(f"Ожидание присутствия элемента: {locator}")
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(locator)
            )
            self.log_action(f"Элемент найден: {locator}")
            return True
        except TimeoutException:
            self.log_action(f"Элемент не найден за {timeout} секунд: {locator}")
            self.browser.save_screenshot(f"element_not_found_{locator}.png")
            return False

    def wait_for_element_visible(self, locator, timeout=3):
        self.log_action(f"Ожидание видимости элемента: {locator}")
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=3):
        self.log_action(f"Поиск множества элементов: {locator}")
        WebDriverWait(self.browser, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.browser.find_elements(*locator)

    def fill_field(self, locator, value):
        self.log_action(f"Заполнение поля {locator} значением: {value}")
        field = self.wait_for_element_visible(locator)
        field.clear()
        field.send_keys(value)
