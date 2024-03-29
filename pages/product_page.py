from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_to_add_to_basket_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_button.click()

    def should_be_product_message_to_basket(self):
        assert self.browser.find_element(*ProductPageLocators.TEXT_PRODUCT).text \
            == self.browser.find_element(*ProductPageLocators.TEXT_BASKET).text , \
            "message is wrong"

    def should_be_price_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text \
            == self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text , \
            "price is wrong"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"    
    
    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"    