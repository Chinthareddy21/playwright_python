from playwright.sync_api import expect
from lib.credentials import Credentials
from lib.url_s import URL_s
from objectRepository.productDetailsObjects import Product_Details

"""
        To test login functionality
        Run command: pytest test/test_Check_Out.py
"""


def test_check_out(login):
    # Constructors
    page = login
    url = URL_s
    product_details = Product_Details

    # Getting homepage after login API status code
    page.request.get(url.Base_url)

    # printing homepage after login API status code
    print(page.request.get(url.Base_url))

    # Selecting category
    page.get_by_role("link", name="Men", exact=True).first.click()
    # Selecting desired item
    page.get_by_role("link", name=Credentials.Product_3).click()
    # Adding item to cart
    expect(page.locator(product_details.Bash_product_UUID)).to_have_text(Credentials.bash_product_UUID)
    expect(page.locator(product_details.Product_code)).to_have_text(Credentials.Product_code)

    # Add to cart screenshot
    page.screenshot(path="Screenshots/product_details/product details.png")
