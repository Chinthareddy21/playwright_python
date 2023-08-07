def test_title(set_up):
        page = set_up
        page.title
        page.screenshot(path="Screenshots/example.png")
        print(page.title())
