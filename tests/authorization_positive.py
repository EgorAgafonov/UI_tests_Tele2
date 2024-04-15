import pytest
from pages.home_page import HomePage
from settings import *
import allure
from allure_commons.types import LabelType
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
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-AUTH_SMS")
    @allure.link("https://msk.tele2.ru", name="https://msk.tele2.ru")
    def test_auth_user_by_sms(self, driver, user_phone=actual_phone):
        """Проверка работы системы авторизации ранее зарегистрированного пользователя посредством входящего SMS
        сообщения с кодом. Ожидаемый результат - после получения SMS и ввода кода, пользователь авторизуется на сайте,
        телефон и аватар пользователя отображаются на странице в правом верхнем углу экрана."""

        with allure.step("Шаг 1: Открыть страницу https://msk.tele2.ru/"):
            page = HomePage(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 2: Нажать кнопку 'Войти'"):
            page.auth_enter_btn_click(driver)
        with allure.step("Шаг 3: Нажать кнопку 'По SMS'"):
            page.auth_by_SMS_btn_click(driver)
        with allure.step("Шаг 4: Ввести моб.номер зарегистрированного пользователя"):
            page.enter_user_phone_num(driver, user_phone)
        with allure.step("Шаг 5: Нажать кнопку 'Далее'"):
            page.press_further_btn_click(driver)
        with allure.step("Шаг 6: Ввести код из полученного SMS сообщения от оператора'"):
            time.sleep(25)
        with allure.step("Шаг 7: Выполнить проверку ожидаемого результата"):
            result = page.get_and_save_access_cookie("access_token")
            if result:
                assert result['name'] != ''
                assert result['value'] != ''
            else:
                raise Exception('Ошибка! Cookie-файл авторизации пользователя не сформирован. Проверьте введенные'
                                'данные пользователя. Иначе создать отчет об ошибке и зарегистрировать в системе '
                                'отслеживания')

    @pytest.mark.auth_password
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка авторизации зарегистрированного пользователя")
    @allure.title("Авторизация пользователя на сайте через SMS сообщение")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-AUTH_PASSWRD")
    @allure.link("https://msk.tele2.ru", name="https://msk.tele2.ru")
    def test_auth_user_by_pass(self, driver, user_phone=actual_phone, user_pass=auth_user_psswrd):
        """Проверка работы системы авторизации ранее зарегистрированного пользователя посредством входящего SMS
        сообщения с кодом. Ожидаемый результат - после получения SMS и ввода кода, пользователь авторизуется на сайте,
        телефон и аватар пользователя отображаются на странице в правом верхнем углу экрана."""

        with allure.step("Шаг 1: Открыть страницу https://msk.tele2.ru/"):
            page = HomePage(driver)
            page.wait_page_loaded()
        with allure.step("Шаг 2: Нажать кнопку 'Войти'"):
            page.auth_enter_btn_click(driver)
        with allure.step("Шаг 3: Нажать кнопку 'По SMS'"):
            page.auth_by_passwrd_btn_click(driver)
        with allure.step("Шаг 4: В поле 'Номер телефона' указать моб.номер зарегистрированного пользователя"):
            page.enter_user_phone_num(driver, user_phone)
        with allure.step("Шаг 5: В поле 'Пароль' указать пароль зарегистрированного пользователя"):
            page.enter_user_password_num(driver, user_pass)
        with allure.step("Шаг 6: Нажать кнопку 'Войти'"):
            page.press_enter_btn_click(driver)


