from lib.url_s import URL_s
from objectRepository.footerObjects import Footer_Objects

"""
        To test login functionality
        Run command: pytest test/test_Footer.py
"""


def test_footer(login):
    # Constructors
    page = login
    url = URL_s

    page.get_by_role("link", name="Online shopping help & FAQs").click()


def test_follow_us(login):
    # Constructors
    page = login
    url = URL_s
    footer = Footer_Objects

    page.go_back()

    page.get_by_role(footer.Facebook).click()
