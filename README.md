# Проект по Автоматизации тестирования на Python с использованием Selenium
## Репозиторий находится на стадии редактирования
## Структура файла с настройками conftest.py:
* ### Поддерживается многоязычность сайтов
* ### Работает с браузерами [Chrome, Firefox]
```python
    import pytest
    from selenium import webdriver
    from selenium.webdriver.common.by import By


    def pytest_addoption(parser):
        parser.addoption('--browser_name', action='store', default="chrome",
                    help="Choose browser: chrome or firefox")
        parser.addoption('--language', action='store', default=None,
                        help="Choose language: '--language=en' or '--language=ru'")

    @pytest.fixture(scope="function")
    def browser(request):
        user_language = request.config.getoption("language")
        browser_name = request.config.getoption("browser_name")
        browser = None
        if browser_name == "chrome":
            print("\nstart chrome browser for test..")
            options = webdriver.ChromeOptions()
            # options.add_argument("--headless") #Открывает браузер в фоновом режиме
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            browser = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            print("\nstart firefox browser for test..")
            fp = webdriver.FirefoxOptions()
            fp.set_preference("intl.accept_languages", user_language)
            browser = webdriver.Firefox(options=fp)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
        yield browser
        print("\nquit browser..")
        browser.quit()

```
## Структура базовой страници base_page.py:
```python
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import NoAlertPresentException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from .locators import BasePageLocators

    import math

    class BasePage():
        def __init__(self, browser, url):
            self.browser = browser
            self.url = url
            
        def elements_are_equal(self,element1,element2):
            if element1 == element2:
                return True
            else:
                return False
            
        def open(self):
            self.browser.get(self.url)
            
        def is_element_present(self,how,what):
            try:
                self.browser.find_element(how,what)
            except (NoSuchElementException):
                return False
            return True
        
        def is_not_element_present(self, how, what, timeout=4):
            try:
                WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
            except TimeoutException:
                return True
            return False
            
        def is_disappeared(self, how, what, timeout=4):
            try:
                WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
            except TimeoutException:
                return False

            return True
            
        
        def solve_quiz_and_get_code(self):
            alert = self.browser.switch_to.alert
            x = alert.text.split(' ')[2]
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
        
        def go_to_login_page(self):
            link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
            link.click()
            #return LoginPage(browser=self.browser, url=self.browser.current_url)
        
        def should_be_login_link(self):
            assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link is not presented'
            
        def go_to_basket(self):
            link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
            link.click()
        
        def should_be_authorized_user(self):
            assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
              
```

## Примеры тестов:
* ### Пробный тест
   Структура файла с тестом test_product_page.py
    ```python
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
        
    

    ```
## Для запуска и проверки заданий на своем компьютере требуется:
### Установленные WebDriver(Chrome или Firefox)
* Создать на своем рабочем столе папку "project"
  ```bash
    mkdir project
  ```
* Перейти в папку "project"
  ```bash
    cd project
  ```
* Скопировать репозиторий на свой компьютер
  ```bash
    git clone https://github.com/kolesnikovvitaliy/pet_project_autotests.git
  ```
* Перейти в папку "pet_project_autotests"
  ```bash
    cd pet_project_autotests
  ```
* Создать и активировать виртуальное окружение
  ```python
    python -m venv env
    source ./env/bin/activate . 
    #python . ./env/bin/activate
  ```
* Установить зависимости
  ```python
    pip install -r requirements.txt
  ```

* Выполнить команду:
  ```python
    pytest -v --tb=line --language=en -m need_review
  ```
  В результате тесты должены сработать без ошибок
  Увидите сообщение:
  ##### == 12 passed, 8 deselected, 1 xfailed ==


