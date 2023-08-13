import re
from playwright.sync_api import expect
from lib.url_s import URL_s
from objectRepository.productFromCategoryObjects import Products_From_Category


"""
        To test login functionality
        Run command: pytest test/test_Product_From_Category.py
"""

def test_Product_From_Category(login):
        # Constructors
        page = login
        url = URL_s

        # Getting homepage after login API status code
        page.request.get(url.Base_url)

        # printing hommepage after login API status code
        print(page.request.get(url.Base_url))

        # Hovering category
        page.get_by_role("link", name="Men", exact=True).hover()
        # Selecting product from hover list
        page.get_by_role("link", name="Watches").first.click()
        # Verifying user is navigated to selected product page
        expect(page.get_by_role("heading", name="Watches")).to_be_visible()

        # Add to cart screenshot
        page.screenshot(path="Screenshots/Product_From_Category/product from Category.png")


def test_Product_From_Components(login):
        # Constructors
        page = login
        product = Products_From_Category
        page.locator(product.component_button).first.click()
        page.locator(product.Component_categories).get_by_text("Men", exact=True).first.click()
        page.locator("li").filter(has_text="JewelleryShop All Mens JewelleryNew InWatchesFashion JewelleryFine JewelleryBrac").locator("span").nth(1).click()
        page.locator("div").filter(has_text=re.compile(r"^Jewellery$")).nth(2).click()
        # Verifying user is navigated to selected product page
        expect(page.get_by_role("heading", name="Watches")).to_be_visible()
