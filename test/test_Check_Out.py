from playwright.sync_api import expect
from lib.credentials import Credentials
from lib.url_s import URL_s
from objectRepository.checkOutObjects import Check_Out

"""
        To test login functionality
        Run command: pytest test/test_Check_Out.py
"""


def test_check_out(login):
    # Constructors
    page = login
    url = URL_s
    check_out = Check_Out

    # Getting homepage after login API status code
    page.request.get(url.Base_url)

    # printing homepage after login API status code
    print(page.request.get(url.Base_url))

    # Selecting category
    page.get_by_role("link", name="Men", exact=True).first.click()
    # Selecting desired item
    page.get_by_role("link", name="Men's Fabiani Canvas Navy Weekender Bag").click()
    # Adding item to cart
    page.get_by_role("button", name="Add to cart").click()

    # Add to cart screenshot
    page.screenshot(path="Screenshots/check_out/added to cart.png")

    # Check out of desired product
    page.get_by_role("button", name="Checkout").click()

    # Verifying navigation to check out page
    expect(page).to_have_url(url.Check_out_page_url)

    # Check out screenshot
    page.screenshot(path="Screenshots/check_out/added to cart.png")

    # Checking the product
    expect(page.locator(check_out.product_name)).to_have_text("Men's Fabiani Canvas Navy Weekender Bag")

    # Checking user email in check out page
    expect(page.locator(check_out.user_email_check)).to_have_text(Credentials.username)
