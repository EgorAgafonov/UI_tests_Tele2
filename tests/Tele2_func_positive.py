import pytest
from pages.main_page import MainPage
from settings import *
from colorama import Fore, Style
import allure
from allure_commons.types import LabelType
from conftest import driver_auth, driver_no_auth
import time


class TestTele2_Functional_Auth_On_Positive:
    """Класс с коллекцией positive UI-тестов функционального тестирования веб-сайта оператора "Tele2" в режиме
    авторизованного пользователя."""

    def test_about_us(self, driver_auth):
        page = MainPage(driver_auth)
