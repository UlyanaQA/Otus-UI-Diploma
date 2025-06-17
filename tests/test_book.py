import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_book_search():
    driver = webdriver.Chrome()
    driver.get("https://www.gutenberg.org/")

    # Поиск книги
    search_box = driver.find_element(By.CLASS_NAME, "search-input")
    search_box.send_keys("Sherlock Holmes")
    search_box.submit()

    # Ожидание результатов
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "booklink"))
    )

    driver.quit()