from playwright.sync_api import Playwright, expect
import pytest

from lib.url_s import URL_s

# Assertions time out
expect.set_options(timeout=60_000)

@pytest.fixture(scope="session")
def Home_page(playwright: Playwright):
    # Browser and page set up
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    url = URL_s
    # Homepage navigation
    page.goto(url.Base_url)

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
