from selenium.webdriver.common.by import By
from .pages.product_page import PageObject
from .pages.cart_page import CartPage
import time



def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = PageObject(browser, link)
    page.open()
    browser.implicitly_wait(5)
    page.should_be_product_page()
    name_product_on_product_page = page.get_to_product_name_in_product_page()
    price_product_on_product_page = page.get_to_product_price_in_product_page()
    #browser.implicitly_wait(5)
    page.go_to_cart_page()
    browser.implicitly_wait(5)
    page.solve_quiz_and_get_code_in_cart_page()
    #browser.implicitly_wait(5)
    cart_page = CartPage(browser, browser.current_url)
    
    browser.implicitly_wait(5)
    cart_page.should_be_cart_page()
    cart_page.should_compare_product_name_and_product_price(name_product_on_product_page, price_product_on_product_page)
    


