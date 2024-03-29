from selenium.webdriver.common.by import By


class MapPageLocators:
    """Класс переменных для определения локаторов элементов на странице "https://yandex.ru/maps"""

    MAP_SEARCH_FIELD = (By.CSS_SELECTOR, "input[placeholder='Поиск мест и адресов']")
    MAP_MY_GEOLOC_BTN = (By.CSS_SELECTOR, "button[aria-label='Моё местоположение']")
    MAP_MY_GEOLOC_NAME = (By.CSS_SELECTOR, "h1[class='home-panel-content-view__header-text']")
