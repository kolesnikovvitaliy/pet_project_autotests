from .base_page import BasePage


from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoinPageLocators, MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "url is not activ"
   
    def should_be_login_form(self):
        assert self.is_element_present(*LoinPageLocators.LOGIN_FORM), "Login_form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoinPageLocators.REGISTER_FORM), "Register_form is not presented"