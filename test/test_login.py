import re 
from playwright.sync_api import expect
from lib.credentials import Credentials
from objectRepository.loginObjects import Login_Objects
from lib.url_s import URL_s


def test_title(set_up):
        page = set_up
        login = Login_Objects
        url = URL_s
        credentials = Credentials
        
        page.screenshot(path="Screenshots/example.png")
        page.locator(login.account_button).click()
        page.locator(login.email_editbox_input).fill(credentials.username)
        page.locator(login.password_editbox_input).fill(credentials.password)
        page.locator(login.login_button).click()
        expect(page).to_have_url(url.Base_url)
        page.screenshot(path="Screenshots/example1.png")
        print(page.title())
