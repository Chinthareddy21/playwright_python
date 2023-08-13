from playwright.sync_api import expect
from lib.credentials import Credentials
from lib.url_s import URL_s
from objectRepository.footerObjects import Footer_Objects

"""
        To test login functionality
        Run command: pytest test/test_Footer.py
"""

# def test_footer(login):
#         # Constructors
#         page = login
#         footer = Footer_Objects
#         url = URL_s

#         # Getting homepage after login API status code
#         page.request.get(url.Base_url)

#         # printing hommepage after login API status code
#         print(page.request.get(url.Base_url))

#         page.locator(footer.FAQ_S).click()

def test_Follow_Us(login):
        
        # Constructors
        page = login
        footer = Footer_Objects
        url = URL_s

        # Getting homepage after login API status code
        page.request.get(url.Base_url)

        # printing hommepage after login API status code
        print(page.request.get(url.Base_url))

        page.locator(footer.Facebook).click()
