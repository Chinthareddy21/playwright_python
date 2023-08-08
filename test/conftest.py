from playwright.sync_api import Playwright, expect
import pytest

from lib.url_s import URL_s


expect.set_options(timeout=60_000)
@pytest.fixture(scope="session")
def set_up(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    url = URL_s
    page.goto(url.Base_url)
    yield page
    browser.close()
