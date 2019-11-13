from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest
import faker
import time

# @pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6",
#                                   pytest.param("7", marks=pytest.mark.xfail),
#                                   "8","9"])
                                  
# def test_guest_can_add_product_to_basket(browser, promo_offer):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
#     page = ProductPage(browser, link)
#     page.open()
#     page.click_to_add_to_basket_button()
#     page.solve_quiz_and_get_code()
#     page.should_be_product_message_to_basket()
#     page.should_be_price_in_basket()

# @pytest.mark.xfail(reason="should be bug, because success message is displayed")
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.click_to_add_to_basket_button()
#     page.should_not_be_success_message()

# def test_guest_cant_see_success_message(browser):
#     link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()   
#     page.should_not_be_success_message()

# @pytest.mark.xfail(reason="should be bug, because success message is not disappeare")
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.click_to_add_to_basket_button()
#     page.should_be_disappeared_message()

# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)  
#     page.open()
#     page.go_to_login_page()


# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_view_basket()
#     page.should_is_not_products_in_the_basket()
#     page.should_be_message_basket_is_emply()

class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        f = faker.Faker()
        email = f.email()
        password = f.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()   
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.click_to_add_to_basket_button()
        page.should_be_product_message_to_basket()
        page.should_be_price_in_basket()

    