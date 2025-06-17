import logging
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import tempfile

from page_objects.advanced_search_page import AdvancedSearchPage
from page_objects.categories_page import CategoriesPage
from page_objects.home_page import HomePage
from page_objects.russian_interest_page import RussianInterestPage
from page_objects.onegin_page import OneginPage

logging.basicConfig(level=logging.INFO)


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="choose browser"
    )
    parser.addoption("--headless", action="store_true", help="headless_mode")
    parser.addoption("--url", action="store", default="https://www.gutenberg.org/")
    parser.addoption(
        "--log_level", action="store", default="INFO", help="choose log level"
    )


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser")
    headless = request.config.getoption("headless")
    url = request.config.getoption("--url")

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    if browser_name in ["chrome", "ch"]:
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # Уникальная папка для профиля
        tmp_dir = tempfile.mkdtemp()
        options.add_argument(f"--user-data-dir={tmp_dir}")

        logger.info(f"инициализация {browser_name} браузера в режиме {'headless' if headless else 'normal'}")
        driver = webdriver.Chrome(options=options)

    elif browser_name in ["edge", "ed"]:
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
        logger.info(f"инициализация {browser_name} браузера в режиме {'headless' if headless else 'normal'}")
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    driver.maximize_window()

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver

@pytest.fixture
def logger(request):
    log_level = request.config.getoption("--log_level")
    logger = logging.getLogger(__name__)
    logger.setLevel(level=log_level)
    return logger


@pytest.fixture
def base_url(request) -> str:
    return request.config.getoption("--url")


@pytest.fixture
def home_page(browser, base_url, logger):
    page = HomePage(browser)
    homepage_url = f"{base_url}"

    logger.info(f"Открытие домашней страницы: {homepage_url}")
    page.open(homepage_url)
    return page

@pytest.fixture
def categories_page(browser, base_url, logger):
    page = CategoriesPage(browser)
    categoriespage_url = f"{base_url}/ebooks/categories"

    logger.info(f"Открытие страницы категорий книг: {categoriespage_url}/ebooks/categories")
    page.open(categoriespage_url)
    return page

@pytest.fixture
def russian_interest_page(browser, base_url, logger):
    page = RussianInterestPage(browser)
    russianpage_url = f"{base_url}/ebooks/bookshelf/473"

    logger.info(f"Открытие страницы Russian Interest: {russianpage_url}")
    page.open(russianpage_url)
    return page

@pytest.fixture
def onegin_page(browser, base_url, logger):
    page = OneginPage(browser)
    oneginpage_url = f"{base_url}/ebooks/23997"

    logger.info(f"Открытие страницы Russian Interest: {oneginpage_url}")
    page.open(oneginpage_url)
    return page

@pytest.fixture
def advancedsearch_page(browser, base_url, logger):
    page = AdvancedSearchPage(browser)
    advancedsearch_url = f"{base_url}/ebooks"

    logger.info(f"Открытие страницы Advanced Search: {advancedsearch_url}")
    page.open(advancedsearch_url)
    return page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.excinfo
    if report:
        browser = item.funcargs.get("browser")
        if browser:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = os.path.join(screenshot_dir, f"{item.name}.png")
            browser.save_screenshot(file_name)
            print(f"\n📸 Скриншот сохранён: {file_name}")
