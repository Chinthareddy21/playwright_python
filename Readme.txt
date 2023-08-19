Installation Setup:
    Commands:
        pip install playwright -- Python setup
        playwright install -- Browsers set up

    Pre-requisites:
        Python --version: 3.10.xx+
        VS code / PyCharm

Tests:
    Run Commands:
        pytest / Python --To run all Tests

        Pytest test/test_Add_To_Cart.py
        pytest test/test_Address_details.py
        pytest test/test_Check_Out.py
        pytest test/test_Footer.py
        pytest test/test_login.py
        pytest test/test_Product_Details.py
        pytest test/test_product_from_menu.py
        pytest test/test_search.py
        pytest test/test_Sign_Up.py

    Description:
        test_Add_To_Cart:
            Add to cart functionalities:
                add to cart
                increase quantity of selected product
                decrease quantity of selected product
                delete selected product in the cart
        
        test_Address_details:
            adding addresses:
                adding new address 

        test_Check_Out:
            check out functionality:
                check out the added item in the cart

        test_footer:
            footer functionality:
                Clicking on footer options -- Faq's options
                clicking on follow us options -- Facebook

        test_login:
            login functionalities:
                logging with valid credentials
                logout
                logging with invalid username
                logging with invalid password

        test_Product_Details:
            product details:
                product details check

        test_product_from_menu:
            product from menu and category(hover):
                select product from category(hover) 
                    --Select product from category(hover) on homepage
                select product from menu 
                    --Select brand items from menu
                    --Select product from the brand
        
        test_search:
            search functionality:
                search for a product from search bar

        test_Sign_Up:
            new user sign up:
                new user sign up
                sign up fail with existing id