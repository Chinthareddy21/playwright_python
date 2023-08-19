import re
from lib.url_s import URL_s
from objectRepository.productFromMenuObjects import Products_From_Menu
from conftest import logger

"""
        To test login functionality
        Run command: pytest test/test_product_from_menu.py
"""


def test_product_from_category(login, logger):
    # Constructors
    page = login
    url = URL_s

    # Getting homepage after login API status code
    page.request.get(url.Base_url)

    # printing homepage after login API status code
    print(page.request.get(url.Base_url))

    # Hovering category
    page.get_by_role("link", name="Men", exact=True).hover()
    logger.info("User hovers on men category on homepage")
    # Selecting product from hover list
    page.get_by_role("link", name="Watches").first.click()
    logger.info("User clicked on watches on hovering items on men category on homepage")
    # Verifying user is navigated to selected product page
    watches_header = page.get_by_role("heading", name="Watches")
    if watches_header.is_visible():
        logger.info("User is navigated to watches page and Header contains watches heading")
    else:
        logger.warning("User is not navigated to watches page")

    # Add to cart screenshot
    page.screenshot(path="Screenshots/Product_From_Category/product from Category hover.png")


def test_product_from_menu(login, logger):
    # Constructors
    page = login
    product = Products_From_Menu

    page.locator(product.Menu_Button).first.click()
    page.locator("li:nth-child(2) > .thefoschini-vtex-tfg-custom-components-1-x-departmentsNavAnchor").click()
    page.get_by_role("link", name="Diesel Men's Spiked Black Plated Chronograph Bracelet Watch SALE Diesel Men's Spiked Black Plated Chronograph Bracelet Watch Diesel From R 3199,00").click()
    page.get_by_role("button", name="Add to cart").click()

    # Add to cart screenshot
    page.screenshot(path="Screenshots/Product_From_Category/product from Menu.png")
