from playwright.sync_api import Playwright
import pytest

@pytest.fixture(scope="session")
def set_up(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bash.com/")
    yield page
    browser.close()
