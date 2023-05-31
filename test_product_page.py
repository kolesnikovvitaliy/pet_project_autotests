from selenium.webdriver.common.by import By
from .pages.product_page import PageObject



def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageObject(browser, link)
    page.open()
    page.should_be_product_page()
    
