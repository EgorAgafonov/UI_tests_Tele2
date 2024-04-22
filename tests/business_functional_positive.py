import pytest
from pages.business_page import ToBusinessPage
from pages.locators import ToBusinessPageLocators
from settings import *
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

    @pytest.mark.tariffs_prices
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка калькулятора тарифов для бизнеса")
    @allure.title("Расчет скидки на тариф при долгосрочном периоде пользования")
    def test_discount_for_duration_use(self, driver):
        """Тест работы селектора выбора продолжительности пользования услугами связи и расчета скидки на странице
        path='/business'. Валидация теста успешна, если при последовательном нажатии на каждый элемент селектора с
        указанным количеством месяцев пользования, стоимость обслуживания на каждом из доступных тарифов будет
        уменьшаться с одновременным отображением значения в карточке тарифа."""

        with allure.step("Шаг 1: Открыть страницу URL=https://msk.tele2.ru/home и дождаться полной загрузки всех "
                         "элементов."):
            page = ToBusinessPage(driver)
            page.for_business_btn_click(driver)
            page.scroll_to_element(element=driver.find_element(*ToBusinessPageLocators.SELECTOR_TITLE))
            page.make_screenshot(file_path=screenshots_folder + "\\discount_for_duration_use_BEFORE.png")
            allure.attach(page.get_page_screenshot_PNG(), name="discount_for_duration_use_BEFORE",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("Шаг 2: Последовательно нажать каждую кнопку селектора 'Выберите срок оплаты и сравните "
                         "скидку'"):
            prices_before = page.check_all_tariffs_prices(driver)
            page.checking_for_a_popup_menu(driver)
            page.payment_periods_selector_btns_click(driver)
            prices_after = page.check_all_tariffs_prices(driver)
        with allure.step("Шаг 3: Выполнить проверку ожидаемого результата"):
            if prices_before[1] > prices_after[1]:
                assert float(prices_before[0]) == float(prices_after[0])
                assert float(prices_before[1]) > float(prices_after[1])
                assert float(prices_before[2]) > float(prices_after[2])
                assert float(prices_before[3]) > float(prices_after[3])
                page.make_screenshot(file_path=screenshots_folder + "\\discount_for_duration_use_AFTER.png")
                allure.attach(page.get_page_screenshot_PNG(), name="discount_for_duration_use_AFTER",
                              attachment_type=allure.attachment_type.PNG)
                page.scroll_up()
                print(f'\nСтоимость бизнес-тарифов без скидки (помесячно): {prices_before}'
                      f'\nСтоимость бизнес-тарифов при оплате за 12 месяцев: {prices_after}')
            else:
                raise Exception(f'Ошибка! Проверить работу калькулятора скидки на тарифы при оплате за указанное число '
                                f'месяцев.\nСоздать баг-репорт и занести ошибку в систему отслеживания.')

    @pytest.mark.vip_number
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Проверка услуги выбора моб. номера для бизнеса")
    @allure.title("Работа кнопки 'Каталог красивых номеров'")
    def test_nice_phone_num_catalog(self, driver):
        """Проверка работы кнопки 'Каталог красивых номеров' для бизнес-абонентов Tele2 и перехода на страницу с
        доступными к приобретению премиальными номерами."""

        with allure.step("Шаг 1: Открыть страницу URL=https://msk.tele2.ru/business и дождаться полной загрузки всех "
                         "элементов."):
            page = ToBusinessPage(driver)
            page.for_business_btn_click(driver)
            page.checking_for_a_popup_menu(driver)
        with allure.step("Шаг 2: Спуститься вниз по странице path=/business до элемента 'Каталог красивых номеров'"):
            page.scroll_to_element(driver.find_element(*ToBusinessPageLocators.VIP_NUMBERS_BANNER))
            page.make_screenshot(file_path=screenshots_folder + "\\nice_phone_num_catalog_CATALOG_BTN.png")
            allure.attach(page.get_page_screenshot_PNG(), name="nice_phone_num_catalog_CATALOG_BTN",
                          attachment_type=allure.attachment_type.PNG)
            starting_page = page.get_relative_link()
        with allure.step("Шаг 3: Нажать кнопку 'Каталог красивых номеров'"):
            page.vip_numbers_catalog_btn_click()
            page.wait_page_loaded()
            numbers_page = page.get_relative_link()
        with allure.step("Шаг 4: Нажать на элемент '0 ₽'"):
            page.price_0_btn_click()
            price_0 = page.check_and_save_current_nice_nums()
        with allure.step("Шаг 5: Нажать на элемент '1 000 ₽'"):
            page.price_1000_btn_click()
            price_1000 = page.check_and_save_current_nice_nums()
        with allure.step("Шаг 6: Нажать на элемент '3 000 ₽'"):
            page.price_3000_btn_click()
            price_3000 = page.check_and_save_current_nice_nums()
        with allure.step("Шаг 7: Нажать на элемент '15 000 ₽'"):
            page.price_15000_btn_click()
            price_15000 = page.check_and_save_current_nice_nums()
        with allure.step("Шаг 8: Выполнить проверку ожидаемого результата"):
            if starting_page != numbers_page:
                assert price_0 != price_1000
                assert price_1000 != price_3000
                assert price_3000 != price_15000

                for i in range(len(price_15000)):
                    assert price_15000[i] not in price_0  # проверим, что каждый номер за 15000 рубл. не присутствует в
                                                          # каталоге номеров, доступных за 0 рубл.
                print(f"\nСтартовая страница: path={starting_page}"
                      f"\nПереход по ссылке: path={numbers_page}")
            else:
                raise Exception('Ошибка! Проверить работу ссылки элемента "Каталог красивых номеров" и/или корректность'
                                'работы функции добавления номера в каталог соразмерно его стоимости. Создать отчет об '
                                'ошибке и занести в систему отслеживания.')






