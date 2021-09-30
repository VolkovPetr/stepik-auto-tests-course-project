from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Current url does not contain 'login'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
       
    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_form.send_keys(email)
        password_form = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_form.send_keys(password)
        password_form_repeat = self.browser.find_element(*LoginPageLocators.PASSWORD_REPEAT)
        password_form_repeat.send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON).click()
    