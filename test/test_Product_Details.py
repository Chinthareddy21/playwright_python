from playwright.sync_api import expect
from lib.url_s import URL_s
from objectRepository.productDetailsObjects import Product_Details

"""
        To test login functionality
        Run command: pytest test/test_Product_Details.py
"""


def test_check_out(login):
    # Constructors
    page = login
    url = URL_s
    product_details = Product_Details



    # Selecting category
    page.get_by_role("link", name="Men", exact=True).first.click()
    # Selecting desired item
    page.get_by_role("link", name="Men's Fabiani Canvas Navy Weekender Bag").click()
    # Adding item to cart
    expect(page.get_by_role("heading", name="Men's Fabiani Canvas Navy Weekender Bag").locator("span")).to_have_text("Men's Fabiani Canvas Navy Weekender Bag")

    # Add to cart screenshot
    page.screenshot(path="Screenshots/product_details/product details.png")
