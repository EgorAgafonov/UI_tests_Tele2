from selenium.webdriver.common.by import By


class HomePageLocators:
    """Класс переменных для определения локаторов элементов на странице "https://yandex.ru/maps"""

    PRIVATE_CLIENTS_BTN = (By.CSS_SELECTOR, 'a[class="header-navbar-main-line-navigation-item__link '
                                         'gtm-new-navigation-link '
                                         'header-navbar-main-line-navigation-item__link_active"]')
