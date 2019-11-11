from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_to_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_product_message_to_basket()
    page.should_be_price_in_basket()