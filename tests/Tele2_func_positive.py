import pytest
from pages.home_page import HomePage
from settings import *
from colorama import Fore, Style
import allure
from allure_commons.types import LabelType
from conftest import driver_auth, driver_no_auth
import time


class TestTele2_Functional_Auth_ON_Positive:
    """Класс с коллекцией positive UI-тестов функционального тестирования веб-сайта оператора "Tele2" в режиме
    авторизованного пользователя."""

    def test_private_persons_button_click(self, driver_auth):
        """"""
        page = HomePage(driver_auth)
        url_before = page.get_relative_link()
        page.private_clients_btn_click()
        url_after = page.get_relative_link()
        print(url_before, url_after, sep=', ')
        assert url_before != url_after
