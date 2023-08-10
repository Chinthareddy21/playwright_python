from playwright.sync_api import expect, Page
from lib.credentials import Credentials
from lib.url_s import URL_s
from objectRepository.searchObjects import Search
from objectRepository.addToCartObjects import Add_To_Cart

"""
        To test login functionality
        Run command: pytest test/test_login.py
"""

def test_add_to_cart(login):
        # Constructors
        page = login
        search = Search
        add_to_cart = Add_To_Cart
        url = URL_s
        credentials = Credentials

        # Getting homepage after login API status code
        page.request.get(url.Base_url)

        # printing hommepage after login API status code
        print(page.request.get(url.Base_url))

        # Selecting category
        page.get_by_role("link", name="Men", exact=True).first.click()
        # Selecting desired item
        page.get_by_role("link", name=credentials.Product_3).click()
        # Adding item to cart
        page.get_by_role("button", name=add_to_cart.add_to_cart_button).click()

        # Add to cart screenshot
        page.screenshot(path="Screenshots/add_to_cart/added to cart.png")
        