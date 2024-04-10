import pytest
from pages.home_page import HomePage
from settings import *
from colorama import Fore, Style
import allure
from allure_commons.types import LabelType
import time


@pytest.mark.skip("Тест требует ручного ввода кода SMS по время выполнения")
@allure.epic("UI-Tele2_функциональное тестирование UI (позитивные тесты)")
@allure.feature("Авторизация на сайте")
@allure.label("Агафонов Е.А.", "владелец")
@allure.label(LabelType.LANGUAGE, "Python")
@allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
class TestTele2_Authorization_Positive:
    """Класс с коллекцией positive UI-тестов функционального тестирования веб-сайта оператора "Tele2" для проверки
    системы авторизации пользователя."""

    @pytest.mark.auth_SMS
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка авторизации зарегистрированного пользователя")
    @allure.title("Авторизация пользователя на сайте через SMS сообщение")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-AUTHREGUSER")
    @allure.link("https://msk.tele2.ru", name="https://msk.tele2.ru")
    def test_reg_user_SMS_authorization(self, driver, phone_num=user_phone):
        """Проверка работы системы авторизации ранее зарегистрированного пользователя посредством входящего SMS
        сообщения с кодом. Ожидаемый результат - после получения SMS и ввода кода, пользователь авторизуется на сайте,
        телефон и аватар пользователя отображаются на странице в правом верхнем углу экрана."""

        page = HomePage(driver)
        page.auth_enter_btn_click(driver)
        page.auth_by_SMS_btn_click(driver)
        page.enter_user_phone_num(driver, phone_num)
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

    @pytest.mark.private_persons
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка навигационного меню сайта")
    @allure.title("Работа кнопки 'Частным лицам' на странице path=/")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-NAVMENU-01")
    @allure.link("https://msk.tele2.ru/", name="https://msk.tele2.ru/")
    def test_private_persons_button_click(self, driver):
        """Тест работы элемента 'Частным лицам' в главном меню навигации сайта. Ожидаемый результат - переход на
        страницу с path='/home'."""

        with allure.step("Шаг 1: Открыть страницу https://msk.tele2.ru/home"):
            page = HomePage(driver)
        with allure.step("Шаг 2: Нажать элемент 'Частным лицам' в главном меню навигации сайта."):
            page.private_clients_btn_click(driver)
            page.checking_for_a_popup_menu(driver)
            current_url = page.get_relative_link()
        with allure.step("Шаг 3: Выполнить проверку ожидаемого результата"):
            assert current_url == '/home'
            page.make_screenshot(file_path=screenshots_folder + "\\private_persons_button_click_EXPECTED_RES.png")
            allure.attach(page.get_page_screenshot_PNG(), name="private_persons_button_click_EXPECTED_RES",
                          attachment_type=allure.attachment_type.PNG)

    @pytest.mark.more_details
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка переадресации на кнопке 'Подробнее'")
    @allure.title("Работа кнопки 'Подробнее' на странице path=/home")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-MORE_DTLS")
    @allure.link("https://msk.tele2.ru/home", name="https://msk.tele2.ru/home")
    def test_more_details_button_links(self, driver):
        """Тест работы элемента 'Подробнее' на странице path='/home'. Валидация теста успешна, если при нажатии
        элемента 'Подробнее' система адресует пользователя на ресурс с рекламной информацией о текущем тарифе Tele2."""

        with allure.step("Шаг 1: Открыть страницу URL=https://msk.tele2.ru/home и дождаться полной загрузки всех "
                         "элементов."):
            page = HomePage(driver)
            current_path = page.get_relative_link()
            page.make_screenshot(file_path=screenshots_folder + "\\more_details_button_links_BEFORE.png")
            allure.attach(page.get_page_screenshot_PNG(), name="more_details_button_links_BEFORE",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Шаг 2: Нажать на элемент 'Подробнее'"):
            page.more_details_btn_click(driver)
            second_path = page.get_relative_link()
        with allure.step("Шаг 3: Выполнить проверку ожидаемого результата"):
            if current_path != second_path:
                page.make_screenshot(file_path=screenshots_folder + "\\more_details_button_links_AFTER.png")
                allure.attach(page.get_page_screenshot_PNG(), name="more_details_button_links_AFTER",
                              attachment_type=allure.attachment_type.PNG)
                page.private_clients_btn_click(driver)
                page.wait_page_loaded()
            else:
                print('Ошибка! Проверить работу ссылки кнопки "Подробнее" на странице path=/home')
                page.make_screenshot(file_path=screenshots_folder + "\\more_details_button_links_FAILED.png")
                allure.attach(page.get_page_screenshot_PNG(), name="more_details_button_links_FAILED",
                              attachment_type=allure.attachment_type.PNG)
                page.private_clients_btn_click(driver)
                page.wait_page_loaded()

    @pytest.mark.tariffs_prices
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка калькулятора тарифов для частных лиц")
    @allure.title("Расчет стоимости тарифа при покупке более одной sim-карты")
    @allure.testcase("https://msk.tele2.ru/home", "TC-TELE2-TARRIFS_CALC")
    @allure.link("https://msk.tele2.ru/home", name="https://msk.tele2.ru/home")
    def test_SIMs_quantity_price(self, driver):
        """Тест работы селектора выбора количества sim-карт на странице path='/home'. Валидация теста успешна,
        если при последовательном нажатии на каждый элемент селектора с указанным количеством sim-карт к покупке,
        текущая стоимость обслуживания на каждом из доступных тарифов будет уменьшаться с одновременным отображением
        значения в карточке."""

        with allure.step("Шаг 1: Открыть страницу URL=https://msk.tele2.ru/home и дождаться полной загрузки всех "
                         "элементов."):
            page = HomePage(driver)
            page.scroll_to_element(element=page.tariffs_text)
            page.make_screenshot(file_path=screenshots_folder + "\\SIMs_quantity_price_BEFORE_CHANGES.png")
            allure.attach(page.get_page_screenshot_PNG(), name="SIMs_quantity_price_BEFORE_CHANGES",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Шаг 2: Последовательно нажать каждую кнопку селектора выбора количества sim-карт"):
            prices_before = page.check_all_tariffs_prices(driver)
            page.sims_quantity_selector_btns_click(driver)
            prices_after = page.check_all_tariffs_prices(driver)
        with allure.step("Шаг 3: Выполнить проверку ожидаемого результата"):
            if prices_before[0] > prices_after[0]:
                assert float(prices_before[0]) > float(prices_after[0])
                assert float(prices_before[1]) > float(prices_after[1])
                assert float(prices_before[2]) > float(prices_after[2])
                assert float(prices_before[3]) > float(prices_after[3])
                page.make_screenshot(file_path=screenshots_folder + "\\SIMs_quantity_price_AFTER_CHANGES.png")
                allure.attach(page.get_page_screenshot_PNG(), name="SIMs_quantity_price_AFTER_CHANGES",
                              attachment_type=allure.attachment_type.PNG)
                print(f'\nСтоимость тарифа при покупке одной sim-карты: {prices_before}'
                      f'\nСтоимость тарифа при покупке пяти sim-карт: {prices_after}')
            else:
                raise Exception(f'Ошибка! Проверить работу калькулятора тарифов при покупке нескольких sim-карт.\n'
                                f'Создать баг-репорт и занести ошибку в систему отслеживания.')


@allure.epic("UI-Tele2_функциональное тестирование UI (позитивные тесты)")
@allure.feature("В режиме авторизованного пользователя")
@allure.label("Агафонов Е.А.", "владелец")
@allure.label(LabelType.LANGUAGE, "Python")
@allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
class TestTele2_Functional_Auth_ON_Positive:
    """Класс с коллекцией positive UI-тестов функционального тестирования веб-сайта оператора "Tele2" в режиме
    авторизованного пользователя."""

    @pytest.mark.private_persons
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка навигационного меню сайта")
    @allure.title("Работа кнопки 'Частным лицам' на странице path=/")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-NAVMENU-01_AUTH")
    @allure.link("https://msk.tele2.ru/", name="https://msk.tele2.ru/")
    def test_private_persons_button_click(self, driver_auth):
        """Тест работы элемента 'Частным лицам' в главном меню навигации сайта в режиме авторизованного пользователя.
        Ожидаемый результат - переход на страницу с path='/home'."""

        with allure.step("Шаг 1: Открыть страницу https://msk.tele2.ru/home"):
            page = HomePage(driver_auth)
        with allure.step("Шаг 2: Нажать элемент 'Частным лицам' в главном меню навигации сайта."):
            page.private_clients_btn_click(driver_auth)
            page.checking_for_a_popup_menu(driver_auth)
            current_url = page.get_relative_link()
        with allure.step("Шаг 3: Выполнить проверку ожидаемого результата"):
            assert current_url == '/home'
            page.make_screenshot(file_path=screenshots_folder + "\\private_persons_button_click_EXPECTED_RES.png")
            allure.attach(page.get_page_screenshot_PNG(), name="private_persons_button_click_EXPECTED_RES",
                          attachment_type=allure.attachment_type.PNG)

    @pytest.mark.more_details
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка переадресации на кнопке 'Подробнее'")
    @allure.title("Работа кнопки 'Подробнее' на странице path=/home")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-MORE_DTLS_AUTH")
    @allure.link("https://msk.tele2.ru/home", name="https://msk.tele2.ru/home")
    def test_more_details_button_links(self, driver_auth):
        """Тест работы элемента 'Подробнее' на странице path='/home' в режиме авторизованного пользователя. Валидация
        теста успешна, если при нажатии элемента 'Подробнее' система адресует пользователя на ресурс с рекламной
        информацией о текущем тарифе Tele2."""

        with allure.step("Шаг 1: Открыть страницу URL=https://msk.tele2.ru/home и дождаться полной загрузки всех "
                         "элементов."):
            page = HomePage(driver_auth)
            current_path = page.get_relative_link()
            page.make_screenshot(file_path=screenshots_folder + "\\more_details_button_links_BEFORE.png")
            allure.attach(page.get_page_screenshot_PNG(), name="more_details_button_links_BEFORE",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Шаг 2: Нажать на элемент 'Подробнее'"):
            page.more_details_btn_click(driver_auth)
            second_path = page.get_relative_link()
        with allure.step("Шаг 3: Выполнить проверку ожидаемого результата"):
            if current_path != second_path:
                page.make_screenshot(file_path=screenshots_folder + "\\more_details_button_links_AFTER.png")
                allure.attach(page.get_page_screenshot_PNG(), name="more_details_button_links_AFTER",
                              attachment_type=allure.attachment_type.PNG)
                page.private_clients_btn_click(driver_auth)
                page.wait_page_loaded()
            else:
                print('Ошибка! Проверить работу ссылки кнопки "Подробнее" на странице path=/home')
                page.make_screenshot(file_path=screenshots_folder + "\\more_details_button_links_FAILED.png")
                allure.attach(page.get_page_screenshot_PNG(), name="more_details_button_links_FAILED",
                              attachment_type=allure.attachment_type.PNG)
                page.private_clients_btn_click(driver_auth)
                page.wait_page_loaded()

    @pytest.mark.tariffs_prices
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка калькулятора тарифов для частных лиц")
    @allure.title("Расчет стоимости тарифа при покупке более одной sim-карты")
    @allure.testcase("https://msk.tele2.ru/home", "TC-TELE2-TARRIFS_CALC_AUTH")
    @allure.link("https://msk.tele2.ru/home", name="https://msk.tele2.ru/home")
    def test_SIMs_quantity_price(self, driver_auth):
        """Тест работы селектора выбора количества sim-карт на странице path='/home' в режиме авторизованного
        пользователя. Валидация теста успешна, если при последовательном нажатии на каждый элемент селектора с
        указанным количеством sim-карт к покупке, текущая стоимость обслуживания на каждом из доступных тарифов будет
        уменьшаться с одновременным отображением значения в карточке."""

        with allure.step("Шаг 1: Открыть страницу URL=https://msk.tele2.ru/home и дождаться полной загрузки всех "
                         "элементов."):
            page = HomePage(driver_auth)
            page.scroll_to_element(element=page.tariffs_text)
            page.make_screenshot(file_path=screenshots_folder + "\\SIMs_quantity_price_BEFORE_CHANGES.png")
            allure.attach(page.get_page_screenshot_PNG(), name="SIMs_quantity_price_BEFORE_CHANGES",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Шаг 2: Последовательно нажать каждую кнопку селектора выбора количества sim-карт"):
            prices_before = page.check_all_tariffs_prices(driver_auth)
            page.sims_quantity_selector_btns_click(driver_auth)
            prices_after = page.check_all_tariffs_prices(driver_auth)
        with allure.step("Шаг 3: Выполнить проверку ожидаемого результата"):
            if prices_before[0] != prices_after[0]:
                assert float(prices_before[0]) > float(prices_after[0])
                assert float(prices_before[1]) > float(prices_after[1])
                assert float(prices_before[2]) > float(prices_after[2])
                assert float(prices_before[3]) > float(prices_after[3])
                page.make_screenshot(file_path=screenshots_folder + "\\SIMs_quantity_price_AFTER_CHANGES.png")
                allure.attach(page.get_page_screenshot_PNG(), name="SIMs_quantity_price_AFTER_CHANGES",
                              attachment_type=allure.attachment_type.PNG)
                print(f'\nСтоимость тарифа при покупке одной sim-карты: {prices_before}'
                      f'\nСтоимость тарифа при покупке пяти sim-карт: {prices_after}')
            else:
                raise Exception(f'Ошибка! Проверить работу калькулятора тарифов при покупке нескольких sim-карт.\n'
                                f'Создать баг-репорт и занести ошибку в систему отслеживания.')

