from playwright.sync_api import Playwright, expect
import pytest
from lib.url_s import URL_s
from objectRepository.loginObjects import Login_Objects
from lib.credentials import Credentials


# Assertions time out
expect.set_options(timeout=60_000)

@pytest.fixture(scope="module")
def Home_page(playwright: Playwright):
    # Browser and page set up
    browser_Chrome = playwright.chromium.launch(headless=False)
    browser_Firefox = playwright.firefox.launch(headless=False)
    browser_Webkit = playwright.webkit.launch(headless=False)
    browser = browser_Webkit
    context = browser.new_context()
    page = context.new_page()

    url = URL_s
    # Homepage navigation
    page.goto(url.Base_url)
        
    page.get_by_label("Close").click()

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


@pytest.fixture(scope="module")
def login(playwright: Playwright):
    # Browser and page set up
    browser_Chrome = playwright.chromium.launch(headless=False)
    browser_Firefox = playwright.firefox.launch(headless=False)
    browser_Webkit = playwright.webkit.launch(headless=False)
    browser = browser_Webkit
    context = browser.new_context()
    page = context.new_page()
   
    # Constructors
    login = Login_Objects
    url = URL_s
    credentials = Credentials
        
    # Homepage navigation
    page.goto(url.Base_url)
        
    page.get_by_label("Close").click()

    # Getting homepage API status code
    page.request.get(url.Base_url)

    # printing homepage API status code
    print(page.request.get(url.Base_url))

    # Step to login page navigation
    page.locator(login.account_button).click()
    # Getting login page API status code
    page.request.get(url.Login_page_url)
    # printing login page API status code
    print(page.request.get(url.Login_page_url))
        
    # Login page screenshot
    page.screenshot(path="Screenshots/login/login page.png")
    # Entering valid username & password
    page.locator(login.email_editbox_input).fill(credentials.username)
    page.locator(login.password_editbox_input).fill(credentials.password)
    # Clicking on login button
    page.locator(login.login_button).click()

    # User is navigated to homepage after successfully logged in
    expect(page).to_have_url(url.Base_url)
    # Verifying wether user successfully logged in or not 
    expect(page.locator(login.account_button_after_login)).to_have_text("Hello, Skyreaper")

    yield page
    
    # Browser close
    context.close()
    browser.close()
