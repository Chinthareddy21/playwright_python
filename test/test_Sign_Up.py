from playwright.sync_api import expect
from lib.credentials import Credentials
from objectRepository.signupObjects import Sign_Up_Objects
from lib.url_s import URL_s

"""
        To test signup functionality
        Run command: pytest test/test_Sign_Up.py
"""

def test_login_with_valid_credentials(Home_page):
        # Constructors
        page = Home_page
        signUp = Sign_Up_Objects
        url = URL_s
        
        # Step to login page navigation
        page.locator(signUp.account_button).click()

        # Getting login page API status code
        page.request.get(url.Login_page_url)

        # printing login page API status code
        print(page.request.get(url.Login_page_url))

        # Login page screenshot
        page.screenshot(path="Screenshots/sign_Up/login page.png")
        # Clicking on register button
        page.locator(signUp.register_button).click()

        # Entering user name for sign up
        page.locator(signUp.email_editbox_input).click()
        page.locator(signUp.email_editbox_input).fill(Credentials.Email)

        # Clicking on create password button
        page.locator(signUp.create_password_button).click()

        expect(page.locator(signUp.Email_Verification)).to_have_text(Credentials.Email)

        # Login page screenshot
        page.screenshot(path="Screenshots/sign_Up/Signup page.png")
