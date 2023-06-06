from selenium.webdriver.common.by import By

class BasePageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini .btn-default:nth-child(1)')
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CLASS_NAME,'login_form')
    REGISTER_FORM = (By.CLASS_NAME,'register_form')
    EMAIL_FIELD = (By.NAME,'registration-email')
    PASSWORD_FIELD = (By.NAME,'registration-password1')
    REPEAT_PASSWORD_FIELD = (By.NAME,'registration-password2')
    REGISTRATION_BUTTON = (By.NAME,'registration_submit')

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_PAGE_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRODUCT_PAGE_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ADD_TO_CART_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert-success:nth-child(1) .alertinner strong')
    ADD_TO_CART_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-child(1) div.alertinner')
   
class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, '.basket-items')
    BASKET_NO_ITEMS_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    
    
    