import pytest
from pages.main_page import MainPage
from settings import *
from colorama import Fore, Style
import allure
from allure_commons.types import LabelType
from conftest import driver_auth, driver_no_auth
import time


class Test_Tele2_Positive_Auth_Off:
    """Класс с коллекцией positive UI-тестов функционального тестирования веб-сайта оператора "Tele2 в режиме
    неавторизованного пользователя."""

    def test_about_us(self, driver_no_auth):
        page = MainPage(driver_no_auth)
        page.wait_page_loaded()
        time.sleep(10)
