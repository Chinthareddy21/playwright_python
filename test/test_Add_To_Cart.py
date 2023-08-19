"""
        To test login functionality
        Run command: pytest test/test_Add_To_Cart.py
"""


def test_add_to_cart(login, logger):
    # Constructors
    page = login

    # Selecting category
    page.get_by_role("link", name="Men", exact=True).first.click()
    # Selecting desired item
    page.get_by_role("link", name="Men's Fabiani Canvas Navy Weekender Bag").click()
    # Adding item to cart
    page.get_by_role("button", name="Add to cart").click()

    if "1" in page.frame_locator('.zoid-visible').locator('[class="change-quantity__InputValue-bQwA-dl OfyKm"]').text_content():
        logger.info("Item is added to cart")
    else:
        logger.info("Item failed to add to cart")

    # Add to cart screenshot
    page.screenshot(path="Screenshots/add_to_cart/added to cart.png")


def test_adding(login, logger):
    # Constructors
    page = login

    # increasing quantity
    page.frame_locator('.zoid-visible').get_by_alt_text('plus').click()

    if "2" in page.frame_locator('.zoid-visible').locator('[class="change-quantity__InputValue-bQwA-dl OfyKm"]').text_content():
        logger.info("Item quantity in the cart is increased")
    else:
        logger.info("Item quantity in the cart isn\'t increased")

    # Check out screenshot
    page.screenshot(path="Screenshots/add_to_cart/increasing quantity.png")


def test_removing(login, logger):
    # Constructors
    page = login

    # Decreasing quantity
    page.frame_locator('.zoid-visible').get_by_alt_text('minus').click()

    if "1" in page.frame_locator('.zoid-visible').locator(
            '[class="change-quantity__InputValue-bQwA-dl OfyKm"]').text_content():
        logger.info("Item quantity in the cart is decreased")
    else:
        logger.info("Item quantity in the cart isn\'t decreased")

    # Check out screenshot
    page.screenshot(path="Screenshots/add_to_cart/decreasing quantity.png")


def test_deleting(login, logger):
    # Constructors
    page = login

    # Deleting quantity
    page.frame_locator('.zoid-visible').locator('[class="cart-item-details-styled__DeleteIcon-dGLHPX dUlxRa"]').click()

    if not page.frame_locator('.zoid-visible').locator(
            '[class="change-quantity__InputValue-bQwA-dl OfyKm"]').is_visible():
        logger.info("Items in the cart are deleted")
    else:
        logger.info("Items in the cart aren\'t deleted")

    # Check out screenshot
    page.screenshot(path="Screenshots/add_to_cart/deleting item.png")
