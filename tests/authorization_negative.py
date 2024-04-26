import pytest
from pages.home_page import HomePage
from settings import *
import allure
from allure_commons.types import LabelType
import time
from pages.locators import *


@allure.epic("UI-Tele2_функциональное тестирование UI (негативные тесты)")
@allure.feature("Авторизация на сайте")
@allure.label("Агафонов Е.А.", "владелец")
@allure.label(LabelType.LANGUAGE, "Python")
@allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
class TestTele2_Authorization_Negative:
    """Класс с коллекцией негативных UI-тестов функционального тестирования веб-сайта оператора "Tele2" для проверки
    системы авторизации пользователя."""

    @pytest.mark.auth_wrong_number
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Авторизация зарегистрированного пользователя по номеру и паролю")
    @allure.title("Авторизация пользователя с параметризацией неверных значений номера телефона")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-AUTH_PASSWRD")
    @allure.link("https://msk.tele2.ru", name="https://msk.tele2.ru")
    def test_auth_user_by_phone_negative(self, driver, user_phone='9771112222'):
        """Негативный тест работы системы авторизации ранее зарегистрированного пользователя посредством ввода не
        верифицированного номера телефона без указания пароля. Ожидаемый результат - система отказывает в авторизации и
        выводит сервисное сообщение о необходимости ввести пароль."""

        with allure.step("Шаг 1: Открыть страницу https://msk.tele2.ru/"):
            page = HomePage(driver)
        with allure.step("Шаг 2: Нажать кнопку 'Войти'"):
            page.auth_enter_btn_click(driver)
        with allure.step("Шаг 3: Нажать кнопку 'По паролю'"):
            page.auth_by_passwrd_btn_click(driver)
        with allure.step("Шаг 4: В поле 'Номер телефона' указать не верифицированный моб.номер"):
            page.enter_user_phone_num(driver, user_phone)
        with allure.step("Шаг 6: Нажать кнопку 'Войти'"):
            page.press_enter_btn_click()
            error_message = page.checking_enter_psswrd_error_msg()
        with allure.step("Шаг 7: Выполнить проверку ожидаемого результата"):
            assert error_message == 'Необходимо ввести пароль'
