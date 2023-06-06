from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import CartPageLocators
from .product_page import PageObject



class CartPage(BasePage):
    def should_be_cart_page(self):
        # self.should_be_cart_page_url()
        #self.should_not_be_success_message()
        self.should_be_name_product()
        self.should_be_price_product()

    def should_compare_product_name_and_product_price(self, name_product_on_product_page, price_product_on_product_page):
        self.should_compare_product_price(price_product_on_product_page)
        self.should_compare_product_name(name_product_on_product_page)


    # def should_be_cart_page_url(self):
    #     assert "?promo=newYear" in self.url, "url cart_page is not activ"
   
    def should_be_name_product(self):
        assert self.is_element_present(*CartPageLocators.PRODUCT_NAME_IN_CART_PAGE), "name_product on cart_page is not presented"

    def should_be_price_product(self):
        assert self.is_element_present(*CartPageLocators.PRODUCT_PRICE_IN_CART_PAGE), "price_product on cart_page is not presented"

    def get_price_poduct_on_cart_page(self):
        return self.browser.find_element(*CartPageLocators.PRODUCT_PRICE_IN_CART_PAGE).text

    def should_compare_product_price(self, price_product_on_product_page):
        print("price_product_on_product_page : ", price_product_on_product_page)
        print("price_product_on_cart_page : ", self.get_price_poduct_on_cart_page())
        assert price_product_on_product_page == self.get_price_poduct_on_cart_page(), "Цена корзины и товара не совпадает"

    def get_name_poduct_on_cart_page(self):
        return self.browser.find_element(*CartPageLocators.PRODUCT_NAME_IN_CART_PAGE).text

    def should_compare_product_name(self, name_product_on_product_page):
        print("name_product_on_product_page : ", name_product_on_product_page)
        print("name_product_on_cart_page : ", self.get_name_poduct_on_cart_page())
        assert name_product_on_product_page == self.get_name_poduct_on_cart_page(), "Название товара на product_page с товаром на странице cart_page не совпадает"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*CartPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_not_be_success_message(self):
        assert self.is_disappeared(*CartPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"