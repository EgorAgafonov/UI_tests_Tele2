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

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

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

        phone_filed = driver.find_element(*HomePageLocators.PHONE_INPUT_FIELD)
        ActionChains(driver).send_keys_to_element(phone_filed, user_phone).pause(1).perform()

    @staticmethod
    def enter_user_password_num(driver, user_pass: str):
        """Метод для ввода пароля в меню авторизации пользователя на сайте"""

        password_filed = driver.find_element(*HomePageLocators.PASSWORD_INPUT_FIELD)
        ActionChains(driver).send_keys_to_element(password_filed, user_pass).pause(1).perform()

    @staticmethod
    def press_further_btn_click(driver):
        """Метод для нажатия кнопки 'Далее' в меню авторизации пользователя на сайте"""

        further_btn = driver.find_element(*HomePageLocators.FURTHER_BTN)
        further_btn.click()

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






    # def enter_searching_address(self, driver, value: str):
    #     """Поиск топонима на веб-платформе Яндекс.Карты. Передает в поле поиска название(адрес) искомого объекта и
    #     подтверждает действие."""
    #
    #     address_field = driver.find_element(*MapPageLocators.MAP_SEARCH_FIELD)
    #     ActionChains(driver).send_keys_to_element(address_field, value).pause(3).send_keys(Keys.DOWN)\
    #         .send_keys(Keys.ENTER) \
    #         .perform()
    #
    # def zoom_in_map(self, driver, amount="low"):
    #     """Осуществляет нажатие кнопки 'Приблизить' на карте. Для выбора кратности увеличения масштаба карты можно
    #     задать значение аргумента amount равным: 'low', 'medium' или 'high'."""
    #
    #     increase_btn = driver.find_element(*MapPageLocators.MAP_INCREASE_VIEW_SIZE)
    #
    #     if amount == "low":
    #         ActionChains(driver).click(increase_btn).pause(0.5).perform()
    #     elif amount == "medium":
    #         ActionChains(driver).click(increase_btn).pause(0.5).click(increase_btn).pause(0.5).perform()
    #     elif amount == "high":
    #         ActionChains(driver).click(increase_btn).pause(0.5).click(increase_btn).pause(0.5)\
    #                             .click(increase_btn).pause(0.5).perform()
    #     else:
    #         raise Exception(
    #             f"\nОшибка! Методу incrise_map_size() задано некорректное значение параметра amount={amount}!\n"
    #             f"Доступные значения:"
    #             f"\n'low', 'medium' или 'high'")
    #
    # def enter_departure_address(self, driver, value):
    #     """Создание начальной точки маршрута. Через аргумент value передает в поле ввода на карте название(адрес) точки
    #     отправления и подтверждает действие."""
    #
    #     dep_address = driver.find_element(*MapPageLocators.MAP_DEPARTURES_ADDRESS_FIELD)
    #     ActionChains(driver).send_keys_to_element(dep_address, value).pause(3).send_keys(Keys.DOWN).send_keys \
    #         (Keys.ENTER).perform()
    #
    # def check_all_variants_of_arrivals_car(self, driver):
    #     """Метод для получения(парсинга) информации о продолжительности маршрута(ов) на автомобиле, сформированного(ых)
    #     системой. Формирует список расчетного времени по всем вариантам маршрутов. Необходим для валидации теста."""
    #
    #     all_arrivals = driver.find_elements(*MapPageLocators.MAP_EXPECTED_TIME_OF_ARRIVAL_CAR)
    #     list_of_arrivals = []
    #     for i in range(len(all_arrivals)):
    #         arrival_time = all_arrivals[i].text
    #         list_of_arrivals.append(arrival_time)
    #     return list_of_arrivals
    #
    # @staticmethod
    # def choose_panorama_random_view(driver):
    #     """Метод для проверки работы функции отображения панорамы улицы по выбраной на карте точке. Перемещает курсор
    #     мыши в центральную область экрана (считает текущие установки разрешения экрана) и
    #     осуществляет нажатие левой кнопкой мыши для перехода в режим отображения статической панорамы улицы.
    #     ВАЖНО: Данный метод необходимо использовать только в активированном режиме 'Панорамы улиц и фотографии'. Не
    #     зависит от разрешения экрана, установленного в текущей тестовой среде."""
    #
    #     x = (Tk().winfo_screenwidth() // 2) + 100
    #     y = Tk().winfo_screenheight() // 2
    #     action = ActionBuilder(driver)
    #     action.pointer_action.move_to_location(x, y).click()
    #     action.perform()
    #
    # @staticmethod
    # def rotate_street_panorama_view(driver):
    #     """Метод для вращения статического изображения уличной панорамы вокруг наблюдателя. Необходим для валидации
    #     тест-кейса test_street_panorama_btn_click."""
    #
    #     x = (Tk().winfo_screenwidth() // 2)
    #     y = Tk().winfo_screenheight() // 2
    #     x_step = -(x // 2)
    #     y_step = 0
    #     action = ActionBuilder(driver)
    #     action.pointer_action.move_to_location(x, y).click_and_hold().pause(1).move_by(x_step, y_step).release()\
    #         .move_to_location(x, y).click_and_hold().pause(0.5).move_by(x_step, y_step).release()\
    #         .move_to_location(x, y).click_and_hold().pause(0.5).move_by(x_step, y_step).release()\
    #         .move_to_location(x, y).click_and_hold().pause(0.5).move_by(x_step, y_step).release()\
    #         .move_to_location(x, y).click_and_hold().pause(0.5).move_by(x_step, y_step).release()\
    #         .move_to_location(x, y).click_and_hold().pause(0.5).move_by(x_step, y_step).release()\
    #         .move_to_location(x, y).click_and_hold().pause(0.5).move_by(x_step, y_step).release()
    #     action.perform()

    # @staticmethod
    # def enter_departure_metro_station(driver, value: str):
    #     """Метод для определения станции отправления на схеме метро. Параметр value указывает строчное наименование
    #     станции метро и передает его в соответствующее поле ввода на веб-странице."""
    #
    #     departure_station = driver.find_element(*MapPageLocators.MAP_DEPARTURE_METRO_STATION_FIELD)
    #     ActionChains(driver).send_keys_to_element(departure_station, value).pause(1).send_keys(Keys.DOWN)\
    #         .send_keys(Keys.ENTER).perform()

    # @staticmethod
    # def check_all_variants_of_metro_rides(driver):
    #     """Метод для получения(парсинга) информации о всех(либо одном) возможных вариантах поездки между указанными
    #     станциям метро, сформированных системой. Возвращает список с указанной длительностью поездки по каждому(либо
    #     одному)предложенному варианту. Необходим для валидации теста."""
    #
    #     all_metro_rides = driver.find_elements(*MapPageLocators.MAP_METRO_RIDES_DURATION)
    #     list_of_rides_duration = []
    #     for i in range(len(all_metro_rides)):
    #         duration_time = all_metro_rides[i].text
    #         list_of_rides_duration.append(duration_time)
    #     return list_of_rides_duration
