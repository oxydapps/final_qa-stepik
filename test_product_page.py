from pages.product_page import ProductPage
import pytest

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

@pytest.mark.xfail(reason="should be bug, because success message is displayed")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_to_add_to_basket_button()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()   
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="should be bug, because success message is not disappeare")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_to_add_to_basket_button()
    page.should_be_disappeared_message()



