import time
import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver import Keys
from pages.base_page import BasePage
from pages.locators import HomePageLocators
from selenium.common.exceptions import *
from tkinter import *


class HomePage(BasePage):
    """Класс с методами для взаимодействия с элементами страницы URL path=/home"""

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)

        self.driver = driver
        self.tariffs_text = driver.find_element(*HomePageLocators.ELEMENT_HOME_LOCATOR)

    @staticmethod
    def auth_enter_btn_click(driver):
        """Метод для нажатия кнопки 'Войти' для авторизации пользователя на сайте"""

        enter_btn = driver.find_element(*HomePageLocators.ENTER_AUTH_BTN)
        enter_btn.click()

    @staticmethod
    def auth_by_SMS_btn_click(driver):
        """Метод для воздействия на элемент 'Через SMS' в меню авторизации пользователя на сайте"""

        by_sms_btn = driver.find_element(*HomePageLocators.AUTH_BY_SMS_BTN)
        by_sms_btn.click()

    @staticmethod
    def auth_by_passwrd_btn_click(driver):
        """Метод для воздействия на элемент 'По паролю' в меню авторизации пользователя на сайте"""

        by_sms_btn = driver.find_element(*HomePageLocators.AUTH_BY_PASSWRD_BTN)
        by_sms_btn.click()

    @staticmethod
    def enter_user_phone_num(driver, user_phone: str):
        """Метод для ввода телефона в меню авторизации пользователя на сайте"""

        phone_field = driver.find_element(*HomePageLocators.PHONE_INPUT_FIELD)
        ActionChains(driver).send_keys_to_element(phone_field, user_phone).pause(1).perform()

    def check_entered_value_to_phone_field_(self) -> str:
        """"""

        entered_phone_value = self.driver.find_element(*HomePageLocators.PHONE_INPUT_FIELD)
        result = entered_phone_value.get_attribute("value")
        return result




    def close_auth_menu(self):
        """Метод для выхода(закрытия) из меню авторизации пользователя по SMS или паролю."""

        close_btn = self.driver.find_element(*HomePageLocators.CLOSE_AUTH_MENU_BTN)
        close_btn.click()

    def checking_enter_psswrd_error_msg(self) -> str:
        """Метод для проверки наличия сообщения об ошибке - 'Необходимо ввести пароль' в случае авторизации на сайте по
        телефону и паролю."""

        time.sleep(1)
        error_message = self.driver.find_element(*HomePageLocators.ENTER_PASSWRD_ERROR_MSSG).text

        return error_message

    @staticmethod
    def enter_user_password_num(driver, user_pass: str):
        """Метод для ввода пароля в меню авторизации пользователя на сайте"""

        password_filed = driver.find_element(*HomePageLocators.PASSWORD_INPUT_FIELD)
        ActionChains(driver).send_keys_to_element(password_filed, user_pass).pause(1).perform()

    def checking_enter_phone_num_error_msg(self) -> str:
        """Метод для проверки наличия сообщения об ошибке - 'Не введен номер телефона' в случае авторизации на сайте по
        телефону и паролю."""

        time.sleep(1)
        error_message = self.driver.find_element(*HomePageLocators.ENTER_PHONE_NUM_ERROR_MSSG).text

        return error_message

    @staticmethod
    def press_further_btn_click(driver):
        """Метод для нажатия кнопки 'Далее' в меню авторизации пользователя на сайте"""

        further_btn = driver.find_element(*HomePageLocators.FURTHER_BTN)
        further_btn.click()

    def press_enter_btn_click(self):
        """Метод для нажатия кнопки 'Войти' в меню авторизации пользователя по паролю на сайте"""

        enter_btn = self.driver.find_element(*HomePageLocators.ENTER_BY_PASSWRD_BTN)
        enter_btn.click()
        time.sleep(1)

    @staticmethod
    def checking_users_account_data(driver):
        """Метод для проверки отображения на странице учетных данных аккаунта пользователя после успешной процедуры
        авторизации на сайте."""

        users_account_data = driver.find_element(*HomePageLocators.ACCOUNTS_AVATAR_DATA).text

        return users_account_data

    @staticmethod
    def checking_for_a_popup_menu(driver):
        """ Метод для проверки наличия на экране pop-up меню для ознакомления с тарифами, перекрывающее контент. При
        появлении происходит нажатие кнопки 'Не сейчас' и возврат к экрану текущей страницы. При отсутствии меню в
        момент тестирования - тестовая функция выполняется в установленном режиме."""

        try:
            time.sleep(1)
            not_now_btn = driver.find_element(*HomePageLocators.POPMECHANIC_SUBMIT_BTN)
        except WebDriverException:
            pass
        else:
            not_now_btn.click()

    @staticmethod
    def two_factor_auth_menu_cancel(driver):
        """ Метод для проверки наличия на экране pop-up меню для подключения дву-факторной авторизации, перекрывающее
        контент. При появлении происходит нажатие кнопки 'Не сейчас' и возврат к экрану текущей страницы. При отсутствии
         меню в момент тестирования - тестовая функция выполняется в установленном режиме."""

        try:
            time.sleep(1)
            cancel_btn = driver.find_element(*HomePageLocators.TWO_FACTOR_AUTH_CANCEL_BTN)
        except WebDriverException:
            pass
        else:
            cancel_btn.click()

    @staticmethod
    def logout_account_btn_click(driver):
        """Метод для клика на элементе 'Выход из аккаунта' на странице личного кабинета пользователя."""

        logout_account_btn = driver.find_element(*HomePageLocators.LOGOUT_ACCOUNT_BTN)
        logout_account_btn.click()

    @staticmethod
    def private_clients_btn_click(driver):
        """Метод для клика на элементе 'Частным лицам' в главном меню навигации по сайту."""

        private_clients_btn = driver.find_element(*HomePageLocators.PRIVATE_CLIENTS_BTN)
        private_clients_btn.click()

    @staticmethod
    def more_details_btn_click(driver):
        """Метод для клика на элементе 'Подробнее' на странице path=/home"""

        more_details_btn = driver.find_element(*HomePageLocators.TIZER_VIDEO_BTN)
        more_details_btn.click()

    @staticmethod
    def about_dot_btn_click(driver):
        """Метод для клика на элементе 'navigationDot_about' на странице https://evolution.tele2.ru/#about"""

        about_dot_btn = driver.find_element(*HomePageLocators.NAV_DOT_ABOUT)
        about_dot_btn.click()

    @staticmethod
    def mia_dot_btn_click(driver):
        """Метод для клика на элементе 'navigationDot_mia' на странице https://evolution.tele2.ru/#about"""

        mia_dot_btn = driver.find_element(*HomePageLocators.NAV_DOT_MIA)
        mia_dot_btn.click()

    @staticmethod
    def benefits_dot_btn_click(driver):
        """Метод для клика на элементе 'navigationDot_benefits' на странице https://evolution.tele2.ru/#about"""

        benefits_dot_btn = driver.find_element(*HomePageLocators.NAV_DOT_BENEFITS)
        benefits_dot_btn.click()

    @staticmethod
    def connect_to_btn_click(driver):
        """Метод для клика на элементе 'Подключиться' на странице https://evolution.tele2.ru/#about"""

        connect_to_btn = driver.find_element(*HomePageLocators.BENEFITS_CONNECT_BTN)
        connect_to_btn.click()

    @staticmethod
    def sims_quantity_selector_btns_click(driver):
        """Метод для клика по элементам селектора 'Выберите тариф и количество SIM-карт' на странице path=/home.
        Последовательно нажимает на кнопки 2,3,4,5."""

        selector_buttons = driver.find_elements(*HomePageLocators.SIMS_QUANTITY_BTNS)

        for button in selector_buttons:
            ActionChains(driver).click(button).pause(1).perform()

    @staticmethod
    def check_all_tariffs_prices(driver):
        """Метод для получения(парсинга) информации о стоимости обслуживания на каждом тарифе Tele2."""

        prices = driver.find_elements(*HomePageLocators.TARIFFS_CURRENT_PRICES)
        list_or_prices = []
        for price in range(len(prices)):
            price_value = prices[price].text
            list_or_prices.append(price_value)

        return list_or_prices
