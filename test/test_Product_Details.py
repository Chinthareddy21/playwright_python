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

    # Getting homepage after login API status code
    page.request.get(url.Base_url)

    # printing homepage after login API status code
    print(page.request.get(url.Base_url))

    # Selecting category
    page.get_by_role("link", name="Men", exact=True).first.click()
    # Selecting desired item
    page.get_by_role("link", name="Men's Fabiani Canvas Navy Weekender Bag").click()
    # Adding item to cart
    expect(page.locator(product_details.Bash_product_UUID)).to_have_text("6ddb7ab9-9418-4c7e-81cc-6fd2fd1f0c54")
    expect(page.locator(product_details.Product_code)).to_have_text("250202AAHB6")

    # Add to cart screenshot
    page.screenshot(path="Screenshots/product_details/product details.png")
