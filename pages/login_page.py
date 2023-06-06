from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_register_form()
        self.should_be_login_url()
        
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Current url does not contain "login"'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form does not exist'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Registration form does not exist'
    
    def register_new_user(self,email,password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_confirm_field = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_FIELD)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_confirm_field.send_keys(password)
        registration_button.click()
        
        
        
        
        