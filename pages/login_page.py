from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "it is not login url"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "not login form on page"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "not register form on page"

    def register_new_user(self, email, password):
        field_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        field_email.send_keys(email)
        field_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        field_password.send_keys(password)
        field_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        field_password_confirm.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()

        
        
