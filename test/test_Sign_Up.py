from playwright.sync_api import expect
from lib.credentials import Credentials
from objectRepository.signupObjects import Sign_Up_Objects
from lib.url_s import URL_s

"""
        To test signup functionality
        Run command: pytest test/test_Sign_Up.py
"""


def test_sign_up_with_new_email(home_page):
    # Constructors
    page = home_page
    sign_up = Sign_Up_Objects
    url = URL_s

    # Step to login page navigation
    page.locator(sign_up.account_button).click()

    # Getting login page API status code
    page.request.get(url.Login_page_url)

    # printing login page API status code
    print(page.request.get(url.Login_page_url))

    # Login page screenshot
    page.screenshot(path="Screenshots/sign_Up/login page.png")
    # Clicking on register button
    page.locator(sign_up.register_button).click()

    # Entering username for sign up
    page.locator(sign_up.email_editbox_input).click()
    page.locator(sign_up.email_editbox_input).fill(Credentials.Email)

    # Clicking on create password button
    page.locator(sign_up.create_password_button).click()

    expect(page.locator(sign_up.Email_Verification)).to_have_text(Credentials.Email)

    # Login page screenshot
    page.screenshot(path="Screenshots/sign_Up/Signup page.png")


def test_sign_up_with_existing_email(home_page):
    # Constructors
    page = home_page
    sign_up = Sign_Up_Objects

    page.go_back()

    # Entering username for sign up
    page.locator(sign_up.email_editbox_input).click()
    page.locator(sign_up.email_editbox_input).fill(Credentials.username)

    # Clicking on create password button
    page.locator(sign_up.create_password_button).click()

    expect(page.locator(sign_up.error_message)).to_have_text('Existing profile found')

    # Login page screenshot
    page.screenshot(path="Screenshots/sign_Up/Signup error.png")
