import allure
import pytest
from selenium.webdriver.chrome.options import *
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from settings import access_token, session_cookie


@pytest.fixture(scope='session')
def driver():
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
        url = os.getenv("MAIN_URL") or "https://msk.tele2.ru/home"
        driver.get(url)
        driver.implicitly_wait(5)
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

    with allure.step("SETUP 1/3: Определение драйвера и настроек Chrome"):
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    with allure.step("SETUP 2/3: Переход на страницу https://msk.tele2.ru"):
        url = os.getenv("MAIN_URL") or "https://msk.tele2.ru/home"
        driver.get(url)
    with allure.step("SETUP 3/3: Авторизация и проверка пользователя на сайте"):
        driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/div/div/div[1]/div/div/div[2]/button[1]").click()
        driver.add_cookie({"name": "access_token", "value": access_token})
        page = BasePage(driver, url)
        page.wait_page_loaded()
        logged_user_phone = driver.find_element(By.CSS_SELECTOR, "span[class='br']").text
        expected_user_phone = os.getenv("AUTH_USER")
        assert logged_user_phone == expected_user_phone, ("Ошибка авторизации! Проверьте корректность данных "
                                                          "пользователя.")
        yield driver
    with allure.step("TEAR DOWN 1/1: Закрыть браузер Chrome"):
        driver.quit()
