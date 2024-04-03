import pytest
from pages.home_page import HomePage
from settings import *
from colorama import Fore, Style
import allure
from allure_commons.types import LabelType
import time


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
    @allure.title("Работа кнопки 'Частным лицам' на странице path=/home")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-NAVMENU-01")
    @allure.link("https://msk.tele2.ru/home", name="https://msk.tele2.ru/home")
    def test_private_persons_button_click(self, driver_auth):
        """Тест работы элемента 'Частным лицам' в главном меню навигации сайта. Ожидаемый результат - переход на
        страницу с path='/home'."""

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

    @pytest.mark.skip('Тестировать только в момент наличия соответствующего проморолика на сайте!!!')
    @pytest.mark.more_details
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка ссылок на ресурс https://evolution.tele2.ru/#about")
    @allure.title("Работа кнопки 'Подробнее' на странице path=/home")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-NAVMENU-01")
    @allure.link("https://msk.tele2.ru/home", name="https://msk.tele2.ru/home")
    def test_more_details_button_links(self, driver):
        """Тест работы элемента 'Подробнее' на странице path='/home'. Валидация теста успешна, если при нажатии
        элемента 'Подробнее' браузер открывает новую вкладку по URL = https://evolution.tele2.ru/#about c рекламным
        блоком услуг Tele2. При воздействии на элемент 'Подключиться' система адресует пользователя на URl =
        https://msk.tele2.ru/tariffs c действующими тарифами оператора связи."""

        with allure.step("Шаг 1: Открыть страницу URL=https://msk.tele2.ru/home и дождаться полной загрузки всех "
                         "элементов."):
            page = HomePage(driver)
            main_tab = page.get_current_tab_ID_descriptor()
            current_path = page.get_relative_link()
        with allure.step("Шаг 2: Нажать на элемент 'Подробнее'"):
            page.more_details_btn_click(driver)
            page.switch_to_new_browser_tab(starting_page=main_tab)
            page.make_screenshot(file_path=screenshots_folder + "\\more_details_button_links_ABOUT.png")
            allure.attach(page.get_page_screenshot_PNG(), name="more_details_button_links_/#ABOUT",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Шаг 3: На открывшейся вкладке окна нажать на белую точку(about) в левой части экрана"):
            page.about_dot_btn_click(driver)
        with allure.step("Шаг 4: Нажать на белую точку(mia)"):
            page.mia_dot_btn_click(driver)
        with allure.step("Шаг 5: Нажать на белую точку(benefits)"):
            page.benefits_dot_btn_click(driver)
            second_path = page.get_relative_link()
        with allure.step("Шаг 6: Нажать на элемент 'Подключиться'"):
            page.connect_to_btn_click(driver)
            tariffs_path = page.get_relative_link()
        with allure.step("Шаг 7: Выполнить проверку ожидаемого результата"):
            if current_path != second_path:
                assert tariffs_path == '/tariffs'
                page.make_screenshot(file_path=screenshots_folder + "\\more_details_button_links_PASSED.png")
                allure.attach(page.get_page_screenshot_PNG(), name="more_details_button_links_PASSED",
                              attachment_type=allure.attachment_type.PNG)
                page.close_current_browser_tab()
                page.switch_back_to_main_tab(main_window_id=main_tab)
            else:
                print('Ошибка! Проверить работу ссылки элемента "Подключиться" на странице '
                      'URL=https://evolution.tele2.ru/#about.')
                page.make_screenshot(file_path=screenshots_folder + "\\more_details_button_links_FAILED.png")
                allure.attach(page.get_page_screenshot_PNG(), name="more_details_button_links_FAILED",
                              attachment_type=allure.attachment_type.PNG)
                page.close_current_browser_tab()
                page.switch_back_to_main_tab(main_window_id=main_tab)

    @pytest.mark.tariff_black
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка ссылок блока тарифов для частных лиц")
    @allure.title("Работа кнопки 'Подробнее' на странице path=/home")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-NAVMENU-01")
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
