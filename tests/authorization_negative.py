import pytest
from pages.home_page import HomePage
from settings import *
import allure
from allure_commons.types import LabelType
from selenium.common.exceptions import *
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

    @pytest.mark.auth_number_only
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Авторизация зарегистрированного пользователя по номеру и паролю")
    @allure.title("Авторизация пользователя по номеру телефона без указания пароля")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-AUTH_PHONE")
    @allure.link("https://msk.tele2.ru", name="https://msk.tele2.ru")
    def test_auth_only_by_phone_negative(self, driver, phone_num='9771112222'):
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
            page.enter_user_phone_num(driver, phone_num)
        with allure.step("Шаг 5: Нажать кнопку 'Войти'"):
            page.press_enter_btn_click()
            error_message = page.checking_enter_psswrd_error_msg()
        with allure.step("Шаг 6: Выполнить проверку ожидаемого результата"):
            try:
                page.checking_users_account_data(driver)
            except WebDriverException:
                print('\n1) Пользователь не авторизован, данные об аккаунте на странице отсутствуют.')
                assert error_message == 'Необходимо ввести пароль'
                print(f'2) Сообщение "{error_message}" инициировано, в авторизации без указания пароля отказано. '
                      f'\n\nНегативный тест пройден успешно!')
                pass
            else:
                raise Exception('Ошибка! Уведомление о необходимости ввести пароль отсутствует, пользователь '
                                'авторизован без пароля. Создать отчет об ошибке и зарегистрировать её в системе '
                                'отслеживания! ')

    @pytest.mark.auth_password_only
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Авторизация зарегистрированного пользователя по номеру и паролю")
    @allure.title("Авторизация пользователя по паролю без указания телефона")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-AUTH_PASSWRD")
    @allure.link("https://msk.tele2.ru", name="https://msk.tele2.ru")
    def test_auth_only_by_passwrd_negative(self, driver, password='Qw#$33491'):
        """Негативный тест работы системы авторизации ранее зарегистрированного пользователя посредством ввода не
        верифицированного пароля без указания номера телефона. Ожидаемый результат - система отказывает в авторизации и
        выводит сервисное сообщение о необходимости ввести номер мобильного телефона."""

        with allure.step("Шаг 1: Открыть страницу https://msk.tele2.ru/"):
            page = HomePage(driver)
        with allure.step("Шаг 2: Нажать кнопку 'Войти'"):
            page.auth_enter_btn_click(driver)
        with allure.step("Шаг 3: Нажать кнопку 'По паролю'"):
            page.auth_by_passwrd_btn_click(driver)
        with allure.step("Шаг 4: В поле 'Пароль' указать не верифицированное значение пароля"):
            page.enter_user_password_num(driver, password)
        with allure.step("Шаг 5: Нажать кнопку 'Войти'"):
            page.press_enter_btn_click()
            error_message = page.checking_enter_phone_num_error_msg()
        with allure.step("Шаг 6: Выполнить проверку ожидаемого результата"):
            try:
                page.checking_users_account_data(driver)
            except WebDriverException:
                print('\n1) Пользователь не авторизован, данные об аккаунте на странице отсутствуют.')

                assert error_message == 'Не введен номер телефона', (f'\nОшибка! Текст сообщения на сайте не '
                                                                     f'соответствует установленному документацией.')
                print(f'2) Сообщение "{error_message}" инициировано, в авторизации без номера телефона отказано. '
                      f'\n\nНегативный тест пройден успешно!')
                pass
            else:
                raise Exception(f'\nОшибка! Уведомление "{error_message}" отсутствует, пользователь авторизовался в '
                                f'системе, выполнен вход в аккаунт.\nСоздать отчет об ошибке и зарегистрировать её в '
                                f'системе отслеживания!')

    @pytest.mark.auth_incorrect_data
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Авторизация зарегистрированного пользователя по номеру и паролю")
    @allure.title("Авторизация пользователя с параметризацией не верифицированных данных пароля и телефона")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-AUTH_PARAMS")
    @allure.link("https://msk.tele2.ru", name="https://msk.tele2.ru")
    @pytest.mark.parametrize('phone', ['', '12e45QW', 'Цу3к89АПпРСьб012', '99127341129388577123995', '!@#$%^&&^*()_+='],
                             ids=['empty_str', 'mix_char-nums_latin', 'mix_char-nums_cyrillic',
                                  'digit_symbols_value>20', 'spec_symbols'])
    @pytest.mark.parametrize('password', ['', '9аъйью1р3тукр1234', '!@#$%^&*()_+='],
                             ids=['empty_str', 'mix_char-nums_cyrillic', 'spec_symbols'])
    def test_auth_by_passwrd_params_negative(self, driver, phone, password='123'):
        """Негативный тест с параметризацией не верифицированных (согласно документации) значений номера телефона и
        пароля пользователя при авторизации на сайте. Ожидаемый результат - система отказывает в авторизации при вводе
        не верифицированных значений, поле номера телефона не принимает буквенных значений и спец. символов."""

        with allure.step("Шаг 1: Открыть страницу https://msk.tele2.ru/"):
            page = HomePage(driver)
        with allure.step("Шаг 2: Нажать кнопку 'Войти'"):
            page.auth_enter_btn_click(driver)
        with allure.step("Шаг 3: Нажать кнопку 'По паролю'"):
            page.auth_by_passwrd_btn_click(driver)
        with allure.step("Шаг 4: В поле 'Номер телефона' указать не верифицированный моб.номер"):
            page.enter_user_phone_num(driver, phone)
        with allure.step("Шаг 5: В поле 'Пароль' указать не верифицированное значение пароля"):
            page.enter_user_password_num(driver, password)
        with allure.step("Шаг 6: Нажать кнопку 'Войти'"):
            page.press_enter_btn_click()
        with allure.step("Шаг 7: Выполнить проверку ожидаемого результата"):
            entered_value = page.check_entered_value_to_phone_field_()
            page.close_auth_menu()
            # 1 Проверка:
            try:
                page.checking_users_account_data(driver)
            except WebDriverException:
                print('\n1) Пользователь не авторизован, данные об аккаунте на странице отсутствуют.')

            # 2 Проверка:
            assert entered_value != phone or entered_value == ''  # поле для ввода телефона (атрибут 'value' тэга input)
            # после нажатия кнопки 'Войти не приняло буквенные
            # символы  и/или пустую строку c номером телефона;
            print(f'2) Поле для ввода номера телефона не приняло параметр phone = {phone} '
                  f'\n\nНегативный тест пройден успешно!')
            page.refresh_page()
            page.checking_for_a_popup_menu(driver)

        #         pass
        #     else:
        #         raise Exception(
        #             f'\nОшибка! Уведомление "{error_message}" отсутствует, пользователь авторизовался в '
        #             f'системе, выполнен вход в аккаунт.\nСоздать отчет об ошибке и зарегистрировать её в '
        #             f'системе отслеживания!')
