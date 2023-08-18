from lib.credentials import Credentials
from lib.url_s import URL_s
from objectRepository.addToCartObjects import Add_To_Cart

"""
        To test login functionality
        Run command: pytest test/test_Add_To_Cart.py
"""


def test_add_to_cart(login):
    # Constructors
    page = login
    url = URL_s
    credentials = Credentials

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
    page.screenshot(path="Screenshots/add_to_cart/added to cart.png")


def test_adding(login):
    # Constructors
    page = login
    add_to_cart = Add_To_Cart

    # increasing quantity
    page.frame_locator('.zoid-visible').get_by_alt_text('plus').click()

    # Check out screenshot
    page.screenshot(path="Screenshots/add_to_cart/increasing quantity.png")


def test_removing(login):
    # Constructors
    page = login
    add_to_cart = Add_To_Cart

    # Decreasing quantity
    page.frame_locator('.zoid-visible').get_by_alt_text('minus').click()

    # Check out screenshot
    page.screenshot(path="Screenshots/add_to_cart/decreasing quantity.png")


def test_deleting(login):
    # Constructors
    page = login
    add_to_cart = Add_To_Cart

    # Deleting quantity
    page.frame_locator('.zoid-visible').locator('[class="cart-item-details-styled__DeleteIcon-dGLHPX dUlxRa"]').click()

    # Check out screenshot
    page.screenshot(path="Screenshots/add_to_cart/deleting item.png")
