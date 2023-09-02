from playwright.sync_api import Playwright, expect
import pytest
from lib.url_s import URL_s
from objectRepository.loginObjects import Login_Objects
from lib.credentials import Credentials
import logging

expect.set_options(timeout=60_000)


@pytest.fixture(scope="session")
def logger(request):
    log_file = "logs.log"
    logger = logging.getLogger("logs.log")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(log_file)
    console_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


@pytest.fixture(scope="class")
def home_page(playwright: Playwright, logger):
    # Browser and page set up
    browser = playwright.chromium.launch(headless=False)
    logger.info("Chrome browser started")
    # browser = playwright.firefox.launch(headless=False)
    # logger.info("Firefox browser started")
    # browser = playwright.webkit.launch(headless=False)    
    # logger.info("Webkit browser started")
    context = browser.new_context()
    page = context.new_page()

    url = URL_s
    # Homepage navigation
    page.goto(url.Base_url)
    if page.url == url.Base_url:
        logger.info("Navigated to homepage & Homepage opened")
    else:
        logger.warning("User is not navigated to homepage")

    page.get_by_label("Close").click()
    logger.info("Ad pop-up closed")

    # Getting homepage API status code
    page.request.get(url.Base_url)

    # printing homepage API status code
    print(page.request.get(url.Base_url))

    # Homepage screenshot
    page.screenshot(path="Screenshots/login/homepage.png")

    yield page

    # Browser close
    context.close()
    browser.close()


@pytest.fixture(scope="class")
def login(playwright: Playwright, logger):
    # Browser and page set up
    browser = playwright.chromium.launch(headless=False)
    logger.info("Chrome browser started")
    # browser = playwright.firefox.launch(headless=False)
    # logger.info("Firefox browser started")
    # browser = playwright.webkit.launch(headless=False)    
    # logger.info("Webkit browser started")
    context = browser.new_context()
    page = context.new_page()

    url = URL_s
    credentials = Credentials
    login = Login_Objects

    # Homepage navigation
    page.goto(url.Base_url)

    if page.url == url.Base_url:
        logger.info("Navigated to homepage & Homepage opened")
    else:
        logger.warning("User is not navigated to homepage")

    page.get_by_label("Close").click()
    logger.info("Ad pop-up closed")

    # Getting homepage API status code
    page.request.get(page.url)

    # printing homepage API status code
    print(page.request.get(page.url))

    # Step to login page navigation
    page.locator(login.account_button).click()
    logger.info("User clicked on account button & Navigated to Login page")

    # Entering valid username & password
    page.locator(login.email_editbox_input).fill(credentials.username)
    logger.info("User entered username")
    page.locator(login.password_editbox_input).fill(credentials.password)
    logger.info("User entered password")
    # Clicking on login button
    page.locator(login.login_button).click()
    logger.info("User clicked on login button")

    # Verifying wether user successfully logged in or not
    account = page.locator(login.account_button_after_login).inner_text()
    if "Hello, Skyreaper" in account:
        logger.info("User logged in successfully & Navigated to homepage")
        logger.info("User name is mentioned in user profile")
    else:
        logger.warning("User is failed to login")

    # Getting homepage API status code
    page.request.get(page.url)

    # printing homepage API status code
    print(page.request.get(page.url))

    yield page

    # Browser close
    context.close()
    browser.close()
