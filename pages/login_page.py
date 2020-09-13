from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in str(self.browser.current_url), "Url address is not correct"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGA_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGA_MAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGA_PASS1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGA_PASS2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGA_BUTTON).click()

    def go_to_login_page(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
