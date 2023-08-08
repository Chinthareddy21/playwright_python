from playwright.sync_api import Playwright, expect
import pytest

from lib.url_s import URL_s


expect.set_options(timeout=60_000)

@pytest.fixture(scope="session")
def Home_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    url = URL_s
    page.goto(url.Base_url)
    page.request.get(url.Base_url)
    print(page.request.get(url.Base_url))
    page.screenshot(path="Screenshots/login/homepage.png")    
    yield page
    browser.close()
