import time
import allure
import pytest
from selenium.webdriver.chrome.options import *
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from settings import *
from cookie import cookie_dict


@pytest.fixture(scope='class')
def driver(request):
    """Pytest-фикстура(декоратор) для выполнения UI-тестов, спроектированных с помощью паттерна PageObjectModel и
    фреймворка Selenium в рамках тестирования платформы "Tele2". Определяет setup-настройки перед началом
    выполнения тестовой сессии, инициализирует запуск драйвера браузера Chrome и передает его в любую тестовую функцию
    коллекции как объект класса webdriver Selenium.

    ВАЖНО: ДАННАЯ ФИКСТУРА ПРЕДВАРИТЕЛЬНО НЕ АВТОРИЗУЕТ ПОЛЬЗОВАТЕЛЯ НА САЙТЕ, НЕОБХОДИМА ДЛЯ ТЕСТИРОВАНИЯ ИНТЕРФЕЙСА В
    РЕЖИМЕ НЕАВТОРИЗОВАННОГО ПОЛЬЗОВАТЕЛЯ !!!"""

    with allure.step("SETUP 1/2: Определить драйвер и настройки Chrome"):
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    with allure.step("SETUP 2/2: Перейти на страницу https://msk.tele2.ru"):
        url = os.getenv("MAIN_URL") or "https://msk.tele2.ru"
        driver.get(url)
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/div/div/div[1]/div/div/div[2]/button[1]").click()
        yield driver
    with allure.step(f"TEAR DOWN: Выполнение тестового набора {request.cls.__name__} окончено."):
        driver.quit()


@pytest.fixture(scope='class')
def driver_auth(request):
    """Pytest-фикстура(декоратор) для выполнения UI-тестов, спроектированных с помощью паттерна PageObjectModel и
    фреймворка Selenium в рамках тестирования платформы "Tele2". Определяет setup-настройки перед началом
    выполнения тестовой сессии, инициализирует запуск драйвера браузера Chrome и передает его в любую тестовую функцию
    коллекции как объект класса webdriver Selenium.

    ВАЖНО: ДАННАЯ ФИКСТУРА ПРЕДВАРИТЕЛЬНО АВТОРИЗУЕТ ПОЛЬЗОВАТЕЛЯ НА САЙТЕ, НЕОБХОДИМА ДЛЯ ТЕСТИРОВАНИЯ ИНТЕРФЕЙСА В
    РЕЖИМЕ АВТОРИЗОВАННОГО ПОЛЬЗОВАТЕЛЯ !!!"""

    with allure.step("SETUP 1/3: Определение драйвера и настроек Chrome"):
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    with allure.step("SETUP 2/3: Переход на страницу https://msk.tele2.ru"):
        url = os.getenv("MAIN_URL") or "https://msk.tele2.ru"
        driver.get(url)
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/div/div/div[1]/div/div/div[2]/button[1]").click()
    with allure.step("SETUP 3/3: Выполнение авторизации и проверка данных пользователя на сайте"):
        page = BasePage(driver, url=url)
        page.wait_page_loaded()
        driver.add_cookie({"name": cookie_dict["name"], "value": cookie_dict["value"]})
        data_base_user_phone = driver.find_element(By.CSS_SELECTOR, 'span[class="br"]').text
        assert data_base_user_phone == auth_user_phone, ("Ошибка авторизации! Проверьте корректность учетных данных"
                                                         "пользователя.")
        yield driver
    with allure.step(f"TEAR DOWN: Выполнение тестового набора {request.cls.__name__} окончено."):
        driver.quit()
