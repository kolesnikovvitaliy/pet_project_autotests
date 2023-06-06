from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), 'There are some items in basket, but should not be'
        
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_NO_ITEMS_MESSAGE), 'The message is not shown, but should be'
        
