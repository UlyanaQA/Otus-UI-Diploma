import logging
import os
import uuid
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from page_objects.home_page import HomePage

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
        logger.info(
            f"инициализация {browser_name} браузера в режиме {'headless' if headless else 'normal'}"
        )
        driver = webdriver.Chrome(options=options)
    elif browser_name in ["edge", "ed"]:
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
        logger.info(
            f"Инициализация {browser_name} браузера в режиме {'headless' if headless else 'normal'}"
        )
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    driver.maximize_window()
    request.addfinalizer(driver.close)

    # logger.info(f"Открытие адреса: {url}")
    # driver.get(url)
    # driver.url = url

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
def admin_login_page(browser, base_url, logger):
    page = HomePage(browser)
    administration_url = f"{base_url}"

    logger.info(f"Открытие страницы админа: {administration_url}")
    page.open(administration_url)
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
