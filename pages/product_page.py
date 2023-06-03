from .base_page import BasePage
from .locators import ProductPageLocators



class PageObject(BasePage):
    def should_be_product_page(self):
        # self.should_be_product_page_url()
        self.should_be_product_name_in_product_page()
        self.should_be_product_price_in_product_page()
        self.should_be_add_cart_link()
        

    # def should_be_product_page_url(self):
    #     assert "?promo=newYear" in self.url, "url product_page is not activ"

    def should_be_product_name_in_product_page(self):      
         assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_PRODUCT_PAGE), "name_product in product_page not present"
    
    def should_be_product_price_in_product_page(self):      
         assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_PRODUCT_PAGE), "price_product in product_page not present"
    
    def should_be_add_cart_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_CART_LINK), "Add_cart link is not presented"

    def get_to_product_name_in_product_page(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_PRODUCT_PAGE).text
        
    def get_to_product_price_in_product_page(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_PRODUCT_PAGE).text

    def go_to_cart_page(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_CART_LINK)
        link.click() 

   

