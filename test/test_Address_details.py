from playwright.sync_api import expect

from objectRepository.addressDetailObjects import Address_details

"""
        To test login functionality
        Run command: pytest test/test_Address_details.py
"""


def test_login_with_valid_credentials(login):
    # Constructors
    page = login
    address = Address_details

    # Verifying wether user successfully logged in or not
    expect(page.locator(address.account_button_after_login)).to_have_text("Hello, Skyreaper")

    # Steps to navigate to user account page
    page.locator(address.account_button_after_login).click()
    page.locator(address.Addresses_Button).click()
    expect(page.locator(address.account_header)).to_have_text("Skyreaper!")

    # Account page screenshot
    page.screenshot(path="Screenshots/Address_Details/account page.png")

    page.locator(address.Add_Address_Button).click()
