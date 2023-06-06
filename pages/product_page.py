from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_item_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()
    
    def product_price_is_displayed_correctly(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_PRICE).text
        product_cart_price = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_PRICE).text
        assert self.elements_are_equal(product_price, product_cart_price), 'Prices are different in cart and product page'
    
    def product_is_added_with_correct_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_NAME).text
        product_cart_name = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_PRODUCT_NAME).text
        assert self.elements_are_equal(product_name, product_cart_name), 'Names are different in cart and product page'
     
    
    def success_message_is_not_present_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
               'Success message is present after adding product to cart'
        
    def success_message_should_not_be_seen_without_adding_product_to_cart(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
               'Success message is present on product page, but it should not'
        
    def success_message_disappeared_after_adding_product_to_cart(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
               'Success message dissapear after adding product to cart'
        
    
    

