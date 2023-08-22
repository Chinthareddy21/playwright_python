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

    expect(page.get_by_text("Men's Fabiani Canvas Navy Weekender Bag FABIANI Qty: 1")).to_be_visible()
    expect(page.get_by_text("FABIANI").nth(2)).to_be_visible()


    # Check out screenshot
    page.screenshot(path="Screenshots/check_out/added to cart.png")