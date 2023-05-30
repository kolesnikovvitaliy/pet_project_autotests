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
            # options.add_argument("--headless")
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
## Примеры тестов:
* ### Пробный тест
   Структура файла с тестом test_main_page.py
    ```python
    from selenium.webdriver.common.by import By


    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        browser.get(link)
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

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
    pytest -v --tb=line --language=en test_main_page.py
  ```
  В результате тест должен сработать без ошибок


