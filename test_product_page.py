from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
import time
import pytest

@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', [*[i for i in range(0, 7)], pytest.param("7", marks=pytest.mark.xfail),"8","9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    product_page = ProductPage(browser,link)
    product_page.open()
    product_page.add_item_to_cart()
    product_page.solve_quiz_and_get_code()
    browser.implicitly_wait(10)
    product_page.product_price_is_displayed_correctly()
    product_page.product_is_added_with_correct_message()

#Test if an unregistered user can see success message without adding any item to cart
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
    product_page = ProductPage(browser,link)
    product_page.open()
    product_page.success_message_should_not_be_seen_without_adding_product_to_cart()

#Test if an unregistered user can see success message after adding product to cart from product page
@pytest.mark.xfail(reason = 'negative test, message is present')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
    product_page = ProductPage(browser,link)
    product_page.open()
    product_page.add_item_to_cart()
    product_page.success_message_is_not_present_after_adding_product_to_basket()

#Test if success message dissapears after adding any item to cart from product page
@pytest.mark.xfail(reason = 'message does not disappear')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
    product_page = ProductPage(browser,link)
    product_page.open()
    product_page.add_item_to_cart()
    product_page.success_message_disappeared_after_adding_product_to_cart()

#Test if an unregistered user can see 'registration\login' link from product page
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()
  
#Test if an unregistered user can go to 'registration/login' page from product page
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser,link)
    product_page.open()
    product_page.go_to_login_page()
     
#Test if an unregistered user can see items in basket from product page without adding anything
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
    product_page = ProductPage(browser,link)
    product_page.open()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_items_in_basket()
    basket_page.should_be_empty_basket_message()

@pytest.mark.user_cart
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        login_page = LoginPage(browser,link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email,'pass123456')
        login_page.should_be_authorized_user()
        self.browser = browser
    
    def test_user_cant_see_success_message(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
        product_page = ProductPage(browser,link)
        product_page.open()
        product_page.success_message_should_not_be_seen_without_adding_product_to_cart()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
        product_page = ProductPage(browser,link)
        product_page.open()
        product_page.success_message_is_not_present_after_adding_product_to_basket()
        
    

       

    
    