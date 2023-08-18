from playwright.sync_api import expect
from lib.credentials import Credentials
from objectRepository.loginObjects import Login_Objects
from lib.url_s import URL_s

"""
        To test login functionality
        Run command: pytest test/test_Login.py
"""


def test_login_with_valid_credentials(home_page):
    # Constructors
    page = home_page
    login = Login_Objects
    url = URL_s
    credentials = Credentials

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

    # Steps to navigate to user account page
    page.locator(login.account_button_after_login).click()
    page.locator(login.profile_details).click()

    # Account page url verification
    expect(page).to_have_url(url.Profile_page_url)
    # Verifying wether username is displayed or not
    expect(page.locator(login.account_header)).to_have_text("Skyreaper!")

    # Getting account page API status code
    page.request.get(url.Profile_page_url)
    # printing account page API status code
    print(page.request.get(url.Profile_page_url))

    # Account page screenshot
    page.screenshot(path="Screenshots/login/account page.png")


def test_logout(home_page):
    # Constructors
    page = home_page
    login = Login_Objects

    # Verifying wether user successfully logged in or not
    expect(page.locator(login.account_button_after_login)).to_have_text("Hello, Skyreaper")

    # Logging out
    page.locator(login.account_button_after_login).click()
    page.locator(login.logout_button).click()

    expect(page.locator(login.email_editbox_input)).to_be_visible()

    # Homepage after successful logout screenshot
    page.screenshot(path="Screenshots/login/login page on logout.png")


def test_login_with_invalid_username(home_page):
    # Constructors
    page = home_page
    login = Login_Objects
    credentials = Credentials

    # Entering invalid username & valid password
    page.locator(login.email_editbox_input).fill(credentials.invalid_username)
    page.locator(login.password_editbox_input).fill(credentials.password)
    # Clicking on login button
    page.locator(login.login_button).click()

    # Verifying wether error message is displayed or not
    expect(page.locator(login.error_message)).to_have_text("We couldn't log you in. Please try again.")
    # Login page screenshot on invalid username
    page.screenshot(path="Screenshots/login/invalid username.png")


def test_login_with_invalid_password(home_page):
    # Constructors
    page = home_page
    login = Login_Objects
    credentials = Credentials

    # Entering valid username & invalid password
    page.locator(login.email_editbox_input).fill(credentials.username)
    page.locator(login.password_editbox_input).fill(credentials.invalid_password)
    # Clicking on login button
    page.locator(login.login_button).click()

    # Verifying wether error message is displayed or not
    expect(page.locator(login.error_message)).to_have_text("We couldn't log you in. Please try again.")
    # Login page screenshot on invalid password
    page.screenshot(path="Screenshots/login/invalid password.png")
