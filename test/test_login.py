from playwright.sync_api import expect
from lib.credentials import Credentials
from objectRepository.loginObjects import Login_Objects
from lib.url_s import URL_s


def test_login_with_valid_credentials(Home_page):
        page = Home_page
        login = Login_Objects
        url = URL_s
        credentials = Credentials
        
        page.locator(login.account_button).click()
        page.screenshot(path="Screenshots/login/login page.png")
        page.locator(login.email_editbox_input).fill(credentials.username)
        page.locator(login.password_editbox_input).fill(credentials.password)
        page.locator(login.login_button).click()

        expect(page).to_have_url(url.Base_url)
        expect(page.locator(login.account_button_after_login)).to_have_text("Hello, Skyreaper")

        page.locator(login.account_button_after_login).click()
        page.locator(login.profile_details).click()

        expect(page).to_have_url(url.Account_page_url)
        expect(page.locator(login.account_header)).to_have_text("Skyreaper!")

        page.request.get(url.Account_page_url)
        print(page.request.get(url.Account_page_url))


        page.screenshot(path="Screenshots/login/account page.png")
