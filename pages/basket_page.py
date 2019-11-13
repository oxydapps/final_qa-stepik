from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
	def should_is_not_products_in_the_basket(self):
	    assert self.is_not_element_present(*BasketPageLocators.CONTENT_BASKET_IS_PRESENT), "Products add in the basket"


	def should_be_message_basket_is_emply(self):
	    language = self.browser.execute_script("return window.navigator.userLanguage || window.navigator.language")
	    if language == 'en':
	        assert self.browser.find_element(*BasketPageLocators.CONTENT_BASKET).text == "Your basket is empty. Continue shopping", "Text message is wrong"
	    else:
	        assert False, "Language site is not English, choose 'en' for test"