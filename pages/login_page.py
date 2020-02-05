from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        does_login_exist=self.browser.current_url
        assert does_login_exist.find("login")!=-1, f"URL doesn't include 'login' part, {does_login_exist}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),"Login form is not presented on the page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM),"Register form is not presented on the page"

    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL),"There's no email field"
        email_field=self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), "There's no password field"
        password_field=self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_field.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD), "There's no confirm password field"
        password_confirm_field=self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD)
        password_confirm_field.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "There's no register button"
        register_button=self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()


