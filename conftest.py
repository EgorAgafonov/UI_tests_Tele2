import allure
import pytest
from selenium.webdriver.chrome.options import *
from selenium import webdriver
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By


load_dotenv()
cookie_value = os.getenv("COOKIES")


@pytest.fixture(scope='session')
def driver_no_auth():
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
    with allure.step("SETUP 2/2: Перейти на страницу https://msk.tele2.ru/"):
        url = os.getenv("MAIN_URL") or "https://msk.tele2.ru"
        driver.get(url)
        driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/div/div/div[1]/div/div/div[2]/button[1]").click()
        yield driver
    with allure.step("TEAR DOWN: Закрыть браузер Chrome"):
        driver.quit()


@pytest.fixture(scope='session')
def driver_auth():
    """Pytest-фикстура(декоратор) для выполнения UI-тестов, спроектированных с помощью паттерна PageObjectModel и
    фреймворка Selenium в рамках тестирования платформы "Tele2". Определяет setup-настройки перед началом
    выполнения тестовой сессии, инициализирует запуск драйвера браузера Chrome и передает его в любую тестовую функцию
    коллекции как объект класса webdriver Selenium.

    ВАЖНО: ДАННАЯ ФИКСТУРА ПРЕДВАРИТЕЛЬНО АВТОРИЗУЕТ ПОЛЬЗОВАТЕЛЯ НА САЙТЕ, НЕОБХОДИМА ДЛЯ ТЕСТИРОВАНИЯ ИНТЕРФЕЙСА В
    РЕЖИМЕ АВТОРИЗОВАННОГО ПОЛЬЗОВАТЕЛЯ !!!"""

    with allure.step("SETUP 1/3: Определить драйвер и настройки Chrome"):
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    with allure.step("SETUP 2/3: Перейти на страницу https://msk.tele2.ru/"):
        url = os.getenv("MAIN_URL") or "https://msk.tele2.ru"
        driver.get(url)
    with allure.step("SETUP 3/3: Перейти на страницу https://msk.tele2.ru/"):
        driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/div/div/div[1]/div/div/div[2]/button[1]").click()
        driver.add_cookie({"name": "access_token", "value": cookie_value})
        yield driver
    with allure.step("TEAR DOWN: Закрыть браузер Chrome"):
        driver.quit()
