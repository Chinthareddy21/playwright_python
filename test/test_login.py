from playwright.sync_api import expect
from lib.credentials import Credentials
from objectRepository.loginObjects import Login_Objects
from lib.url_s import URL_s

"""
        To test login functionality
        Run command: pytest -s test/test_login.py
"""

def test_login_with_valid_credentials(Home_page):
        # Constructors
        page = Home_page
        login = Login_Objects
        url = URL_s
        credentials = Credentials
        
        # Step to login page navigation
        page.locator(login.account_button).click()
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
        expect(page).to_have_url(url.Account_page_url)
        # Verifying wether user name is displayed or not
        expect(page.locator(login.account_header)).to_have_text("Skyreaper!")

        # Getting account page API status code 
        page.request.get(url.Account_page_url)
        # printing account page API status code
        print(page.request.get(url.Account_page_url))

        # Account page screenshot
        page.screenshot(path="Screenshots/login/account page.png")
