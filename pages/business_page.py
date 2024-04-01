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

    @staticmethod
    def checking_for_a_popup_menu(driver):
        """ Метод для проверки наличия на экране pop-up меню для ознакомления с тарифами, перекрывающее контент. При
        появлении происходит нажатие кнопки 'Не сейчас' и возврат к экрану текущей страницы. При отсутствии меню в
        момент тестирования - тестовая функция выполняется в установленном режиме."""

        try:
            time.sleep(3)
            not_now_btn = driver.find_element(*HomePageLocators.POPMECHANIC_SUBMIT_BTN)
        except WebDriverException:
            pass
        else:
            not_now_btn.click()