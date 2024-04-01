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
@allure.feature("В режиме неавторизованного пользователя")
@allure.label("Агафонов Е.А.", "владелец")
@allure.label(LabelType.LANGUAGE, "Python")
@allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
class TestTele2_Functional_Auth_OFF_Positive:
    """Класс с коллекцией positive UI-тестов функционального тестирования веб-сайта оператора "Tele2" в режиме
    неавторизованного пользователя."""

    @pytest.mark.mainnavmenu_01
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Главное навигационное меню сайта")
    @allure.title("Нажать на элемент 'Частным лицам'")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-NAVMENU-01")
    @allure.link("https://msk.tele2.ru/home", name="https://msk.tele2.ru/home")
    def test_private_persons_button_click(self, driver):
        """Тест работы элемента 'Частным лицам' в главном меню навигации сайта. Ожидаемый результат - переход на
        страницу с path='/home'."""

        page = HomePage(driver)
        url_before = page.get_relative_link()
        page.private_clients_btn_click(driver)
        page.wait_page_loaded()
        page.checking_for_a_popup_menu(driver)
        url_after = page.get_relative_link()

        assert url_before != url_after
