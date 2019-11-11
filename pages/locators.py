from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
	BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	TEXT_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
	TEXT_BASKET = (By.CSS_SELECTOR, "div.alertinner > strong:first-child")
	PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main p.price_color")
	PRICE_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong:first-child")


