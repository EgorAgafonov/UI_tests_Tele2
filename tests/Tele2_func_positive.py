import pytest
from pages.home_page import HomePage
from settings import *
from colorama import Fore, Style
import allure
from allure_commons.types import LabelType
from conftest import driver_auth, driver
import time


class TestTele2_Functional_Auth_OFF_Positive:
    """Класс с коллекцией positive UI-тестов функционального тестирования веб-сайта оператора "Tele2" в режиме
    неавторизованного пользователя."""

    def test_private_persons_button_click(self, driver):
        """Тест работы элемента 'Частным лицам' в главном меню навигации сайта. Ожидаемый результат - переход на
        страницу с path='/home'."""

        page = HomePage(driver)
        page.wait_page_loaded()
        url_before = page.get_relative_link()
        page.private_clients_btn_click(driver)
        url_after = page.get_relative_link()

        assert url_before != url_after

    def test_for_business_button_click(self, driver):
        """Тест работы элемента 'Бизнесу' в главном меню навигации сайта. Ожидаемый результат - переход на
        страницу с path='/business'."""

        page = HomePage(driver)
        page.wait_page_loaded()
        url_before = page.get_relative_link()
        page.for_business_btn_click(driver)
        url_after = page.get_relative_link()

        assert url_before != url_after
