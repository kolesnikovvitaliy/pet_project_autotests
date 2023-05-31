from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class PageObject(BasePage):

    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_add_cart_link()
        self.go_to_cart_page()
        self.solve_quiz_and_get_code()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_product_url(self):
        assert "?promo=newYear" in self.url, "url is not promo"
    
    def should_be_add_cart_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_CART_LINK), "Add_cart link is not presented"
    
    def go_to_cart_page(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_CART_LINK)
        link.click() 

