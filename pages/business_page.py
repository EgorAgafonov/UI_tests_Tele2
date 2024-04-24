import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver import Keys
from pages.base_page import BasePage
from pages.locators import *
from selenium.common.exceptions import *


class ToBusinessPage(BasePage):
    """Класс с методами для взаимодействия с элементами страницы URL path=/business"""

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

        self.driver = driver

    @staticmethod
    def for_business_btn_click(driver):
        """Метод для клика на элементе 'Бизнесу' в главном меню навигации по сайту."""

        private_clients_btn = driver.find_element(*ToBusinessPageLocators.FOR_BUSINESS_BTN)
        private_clients_btn.click()

    @staticmethod
    def checking_for_a_popup_menu(driver):
        """ Метод для проверки наличия на экране pop-up меню для ознакомления с тарифами, перекрывающее контент. При
        появлении происходит нажатие кнопки 'Не сейчас' и возврат к экрану текущей страницы. При отсутствии меню в
        момент тестирования - тестовая функция выполняется в установленном режиме."""

        try:
            time.sleep(2)
            not_now_btn = driver.find_element(*HomePageLocators.POPMECHANIC_SUBMIT_BTN)
        except WebDriverException:
            pass
        else:
            not_now_btn.click()

    @staticmethod
    def payment_periods_selector_btns_click(driver):
        """Метод для клика по элементам селектора 'Выберите срок оплаты' на странице path=/business.
        Последовательно нажимает на каждую кнопки со сроком оплаты."""

        selector_buttons = driver.find_elements(*ToBusinessPageLocators.SELECTOR_PAYMENT_PERIODS)

        for button in selector_buttons:
            ActionChains(driver).click(button).pause(1).perform()

    @staticmethod
    def check_all_tariffs_prices(driver):
        """Метод для получения(парсинга) информации о стоимости обслуживания на каждом бизнес-тарифе Tele2."""

        prices = driver.find_elements(*ToBusinessPageLocators.BUSINESS_TARIFFS_CURRENT_PRICES)
        list_or_prices = []
        for price in range(len(prices)):
            price_value = prices[price].text[:3]
            list_or_prices.append(price_value)

        return list_or_prices

    def vip_numbers_catalog_btn_click(self):
        """Метод для клика на кнопке 'Каталог красивых номеров' на странице path=/business'"""

        vip_nums_catalog = self.driver.find_element(*ToBusinessPageLocators.VIP_NUMBERS_CATALOG_BTN)
        vip_nums_catalog.click()

    def check_and_save_current_nice_nums(self) -> list:
        """Метод для проверки присутствия на странице тэгов с доступными для приобретения телефонными номерами. Парсит
        и сохраняет в список первые 20 номеров за выбранную стоимость."""

        nice_nums_list = []
        nice_nums = self.driver.find_elements(*ToBusinessPageLocators.VIP_PHONE_NUMBERS)
        for num in range(len(nice_nums)):
            result = nice_nums[num].text
            nice_nums_list.append(result)

        return nice_nums_list

    def check_search_results(self) -> str:
        """"""

        searching_result = self.driver.find_element(*ToBusinessPageLocators.VIP_PHONE_NUMBERS).text

        return searching_result

    def price_0_btn_click(self):
        """Метод для клика на элементе '0₽' на странице path=/business/numbers"""

        price_btn_0 = self.driver.find_element(*ToBusinessPageLocators.NUM_PRICE_0)
        ActionChains(self.driver).click(price_btn_0).pause(1).perform()

    def price_1000_btn_click(self):
        """Метод для клика на элементе '1000₽' на странице path=/business/numbers"""

        price_btn_1000 = self.driver.find_element(*ToBusinessPageLocators.NUM_PRICE_1000)
        ActionChains(self.driver).click(price_btn_1000).pause(1).perform()

    def price_3000_btn_click(self):
        """Метод для клика на элементе '3000₽' на странице path=/business/numbers"""

        price_btn_3000 = self.driver.find_element(*ToBusinessPageLocators.NUM_PRICE_3000)
        ActionChains(self.driver).click(price_btn_3000).pause(1).perform()

    def price_15000_btn_click(self):
        """Метод для клика на элементе '15000₽' на странице path=/business/numbers"""

        price_btn_15000 = self.driver.find_element(*ToBusinessPageLocators.NUM_PRICE_15000)
        ActionChains(self.driver).click(price_btn_15000).pause(1).perform()

    def enter_vip_num_to_search(self, mobile_number: str):
        """Метод ввода в поле поиска мобильного номера на странице path=/business/numbers. Обязательный аргумент
        принимает строковое значение номера для поиска."""

        search_field = self.driver.find_element(*ToBusinessPageLocators.VIP_NUM_SEARCH_FIELD)
        ActionChains(self.driver).send_keys_to_element(search_field, mobile_number).pause(3).perform()

