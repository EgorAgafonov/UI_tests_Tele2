import pytest
from pages.home_page import HomePage
from pages.business_page import ToBusinessPage
from settings import *
from colorama import Fore, Style
import allure
from allure_commons.types import LabelType
from conftest import driver_auth, driver
import time


@allure.epic("UI-Tele2_функциональное тестирование UI (позитивные тесты)")
@allure.feature("Авторизация на сайте")
@allure.label("Агафонов Е.А.", "владелец")
@allure.label(LabelType.LANGUAGE, "Python")
@allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
class TestTele2_Authorization_Positive:
    """Класс с коллекцией positive UI-тестов функционального тестирования веб-сайта оператора "Tele2" для проверки
    системы авторизации пользователя."""

    # @pytest.mark.skip("Тест требует ручного ввода кода SMS по время выполнения")
    @pytest.mark.auth_SMS
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка авторизации зарегистрированного пользователя")
    @allure.title("Авторизация пользователя на сайте через SMS сообщение")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-AUTHREGUSER")
    @allure.link("https://msk.tele2.ru", name="https://msk.tele2.ru")
    def test_reg_user_SMS_authorization(self, driver, user_phone=actual_phone):
        """Проверка работы системы авторизации ранее зарегистрированного пользователя посредством входящего SMS
        сообщения с кодом. Ожидаемый результат - после получения SMS и ввода кода, пользователь авторизуется на сайте,
        телефон и аватар пользователя отображаются на странице в правом верхнем углу экрана."""

        page = HomePage(driver)
        page.auth_enter_btn_click(driver)
        page.auth_by_SMS_btn_click(driver)
        page.enter_user_phone_num(driver, user_phone)
        page.press_further_btn_click(driver)
        time.sleep(25)
        result = page.get_and_save_access_cookie("access_token")

        assert result != ''


@allure.epic("UI-Tele2_функциональное тестирование UI (позитивные тесты)")
@allure.feature("В режиме неавторизованного пользователя")
@allure.label("Агафонов Е.А.", "владелец")
@allure.label(LabelType.LANGUAGE, "Python")
@allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
class TestTele2_Functional_Auth_OFF_Positive:
    """Класс с коллекцией positive UI-тестов функционального тестирования веб-сайта оператора "Tele2" в режиме
    неавторизованного пользователя."""

    @pytest.mark.mainnavmenu_02
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Главное навигационное меню сайта")
    @allure.title("Нажать на элемент 'Бизнесу'")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-NAVMENU-02")
    @allure.link("https://msk.tele2.ru/business", name="https://msk.tele2.ru/business")
    def test_for_business_button_click(self, driver):
        """Тест работы элемента 'Бизнесу' в главном меню навигации сайта. Ожидаемый результат - переход на
        страницу с path='/business'."""

        page = ToBusinessPage(driver)
        url_before = page.get_relative_link()
        page.for_business_btn_click(driver)
        page.wait_page_loaded()
        page.checking_for_a_popup_menu(driver)
        url_after = page.get_relative_link()
        assert url_before != url_after
