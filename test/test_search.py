from playwright.sync_api import expect
from lib.credentials import Credentials
from lib.url_s import URL_s
from objectRepository.searchObjects import Search

"""
        To test login functionality
        Run command: pytest test/test_search.py
"""


def test_search_1(login):
    # Constructors
    page = login
    search = Search
    url = URL_s
    credentials = Credentials

    # Getting homepage after login API status code
    page.request.get(url.Base_url)

    # printing homepage after login API status code
    print(page.request.get(url.Base_url))

    # User search for desired product
    page.get_by_placeholder(search.search_editbox).click()
    page.get_by_placeholder(search.search_editbox).fill(credentials.Product_1)
    page.get_by_placeholder(search.search_editbox).press("Enter")

    # Verifying wether user is navigated to desired search results page
    expect(page).to_have_title(credentials.Product_1_search_title)

    # results for product 1 screenshot
    page.screenshot(path="Screenshots/search/search results(product 1).png")


def test_search_2(login):
    # Constructors
    page = login
    search = Search
    credentials = Credentials

    page.go_back()

    # User search for desired product
    page.get_by_placeholder(search.search_editbox).click()
    page.get_by_placeholder(search.search_editbox).fill(credentials.Product_2)
    page.get_by_placeholder(search.search_editbox).press("Enter")

    # Verifying wether user is navigated to desired search results page
    expect(page).to_have_title(credentials.Product_2_search_title)

    # results for product 2 screenshot
    page.screenshot(path="Screenshots/search/search results(product 2).png")
