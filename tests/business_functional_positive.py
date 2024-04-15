import pytest
from pages.business_page import ToBusinessPage
from settings import *
from colorama import Fore, Style
import allure
from allure_commons.types import LabelType
from conftest import driver_auth, driver
import time


@allure.epic("UI-Tele2_функциональное тестирование UI (позитивные тесты)")
@allure.feature("В режиме неавторизованного пользователя")
@allure.label("Агафонов Е.А.", "владелец")
@allure.label(LabelType.LANGUAGE, "Python")
@allure.label(LabelType.FRAMEWORK, "Pytest", "Selenium")
class TestTele2_Functional_Auth_OFF_Positive:
    """Класс с коллекцией positive UI-тестов функционального тестирования веб-сайта оператора "Tele2" в режиме
    неавторизованного пользователя."""

    @pytest.mark.to_business
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка навигационного меню сайта")
    @allure.title("Нажать на элемент 'Бизнесу'на странице path=/")
    @allure.testcase("https://msk.tele2.ru/", "TC-TELE2-NAVMENU-02")
    @allure.link("https://msk.tele2.ru/business", name="https://msk.tele2.ru/business")
    def test_to_business_button_click(self, driver):
        """Тест работы элемента 'Бизнесу' в главном меню навигации сайта. Ожидаемый результат - переход на
        страницу с path='/business'."""

        with allure.step("Шаг 1: Открыть страницу https://msk.tele2.ru/"):
            page = ToBusinessPage(driver)
            url_before = page.get_relative_link()
        with allure.step("Шаг 2: Нажать элемент 'Бизнесу' в главном меню навигации сайта."):
            page.for_business_btn_click(driver)
            page.checking_for_a_popup_menu(driver)
            page.wait_page_loaded()
            page.checking_for_a_popup_menu(driver)
            url_after = page.get_relative_link()
        with allure.step("Шаг 3: Выполнить проверку ожидаемого результата"):
            assert url_before != url_after
            page.make_screenshot(file_path=screenshots_folder + "\\to_business_button_click_EXPECTED_RES.png")
            allure.attach(page.get_page_screenshot_PNG(), name="to_business_button_click_EXPECTED_RES",
                          attachment_type=allure.attachment_type.PNG)