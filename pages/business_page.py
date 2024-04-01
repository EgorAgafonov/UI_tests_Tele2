import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver import Keys
from pages.base_page import BasePage
from pages.locators import *
from selenium.common.exceptions import *
from tkinter import *


class ToBusinessPage(BasePage):
    """Класс с методами для взаимодействия с элементами страницы URL path=/business"""

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    @staticmethod
    def for_business_btn_click(driver):
        """Метод для клика на элементе 'Бизнесу>' в главном меню навигации по сайту."""

        private_clients_btn = driver.find_element(*ToBusinessPageLocators.FOR_BUSINESS_BTN)
        private_clients_btn.click()