from .base_page import BasePage
from .locators import LoginPageLocators
import re
import time 
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert re.match(r".*(login/)$", self.browser.current_url), "Page doesn't end in 'login/'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not present"

    def register_new_user(self, email, password):
        self.should_be_register_form()
        self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASS_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()


