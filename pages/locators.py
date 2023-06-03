from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoinPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_CART_LINK = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_IN_PRODUCT_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE_IN_PRODUCT_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main p.price_color")

class CartPageLocators():
    PRODUCT_NAME_IN_CART_PAGE = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE_IN_CART_PAGE = (By.CSS_SELECTOR, ".alertinner p strong")
    