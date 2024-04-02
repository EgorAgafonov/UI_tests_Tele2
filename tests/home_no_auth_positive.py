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

    @pytest.mark.mainnavmenu_01
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка навигационного меню сайта")
    @allure.title("Нажать на элемент 'Частным лицам'")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-NAVMENU-01")
    @allure.link("https://msk.tele2.ru/home", name="https://msk.tele2.ru/home")
    def test_private_persons_button_click(self, driver):
        """Тест работы элемента 'Частным лицам' в главном меню навигации сайта. Ожидаемый результат - переход на
        страницу с path='/home'."""

        page = HomePage(driver)
        page.private_clients_btn_click(driver)
        page.wait_page_loaded()
        page.checking_for_a_popup_menu(driver)
        current_url = page.get_relative_link()

        assert current_url == '/home'

    @pytest.mark.more_details
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка ссылок рекламного блока сайта")
    @allure.title("Нажать на элемент 'Подробнее'")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-NAVMENU-01")
    @allure.link("https://msk.tele2.ru/home", name="https://msk.tele2.ru/home")
    def test_more_details_button_links(self, driver):
        """Тест работы элемента 'Подробнее' на странице path='/home'. Валидация теста положительна, если при нажатии
        элемента 'Подробнее' браузер открывает новую вкладку по URL = https://evolution.tele2.ru/#about c рекламным
        блоком услуг Tele2. При воздействии на элемент 'Подключиться' система адресует пользователя на URl =
        https://msk.tele2.ru/tariffs c действующими тарифами оператора связи."""

        with allure.step("Шаг 1: Открыть страницу URL=https://msk.tele2.ru/home и дождаться полной загрузки всех "
                         "элементов."):
            page = HomePage(driver)
            page.make_screenshot(file_path=screenshots_folder + "\\more_details_button_links_HOME.png")
            allure.attach(page.get_page_screenshot_PNG(), name="more_details_button_links_/HOME",
                          attachment_type=allure.attachment_type.PNG)
            main_tab = page.get_current_tab_ID_descriptor()
        with allure.step("Шаг 2: Нажать на элемент 'Подробнее' с лева от центра страницы"):
            page.more_details_btn_click(driver)
            page.switch_to_new_browser_tab(starting_page=main_tab)
            page.make_screenshot(file_path=screenshots_folder + "\\more_details_button_links_ABOUT.png")
            allure.attach(page.get_page_screenshot_PNG(), name="more_details_button_links_/#ABOUT",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Шаг 4: Нажать на второй снизу дот(точку) белого цвета"):
            page.about_dot_btn_click(driver)
        with allure.step("Шаг 3: На открывшейся вкладке окна нажать на дот(точку) розового цвета в левой части экрана"):
            page.mia_dot_btn_click(driver)
        with allure.step("Шаг 3: На открывшейся вкладке окна нажать на дот(точку) розового цвета в левой части экрана"):
            page.benefits_dot_btn_click(driver)
        with allure.step("Шаг 5: Нажать на элемент 'Подключиться'"):
            page.connect_to_btn_click(driver)
            page.make_screenshot(file_path=screenshots_folder + "\\more_details_button_links_CONNECT_TO.png")
            allure.attach(page.get_page_screenshot_PNG(), name="more_details_button_links_CONNECT_TO",
                          attachment_type=allure.attachment_type.PNG)
        # with allure.step("Шаг 6: Выполнить проверку ожидаемого результата"):
        #     assert starting_path != new_tab_path
        #     assert tariffs_path == '/tariffs'








