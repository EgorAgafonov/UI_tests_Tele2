from selenium.webdriver.common.by import By


class HomePageLocators:
    """Класс переменных для определения локаторов элементов страницы "https://msk.tele2.ru/home"""

    POPMECHANIC_SUBMIT_BTN = (By.CSS_SELECTOR, 'button[class="popmechanic-submit popmechanic-submit-close"]')
    PRIVATE_CLIENTS_BTN = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div['
                                     '1]/div/div/div/div/header/section[1]/ul/li[1]/a')
    TIZER_VIDEO_BTN = (By.CSS_SELECTOR, 'span[class="btn tizer-video-announcement__link btn-white"]')
    NAV_DOT_ABOUT = (By.CSS_SELECTOR, 'div[data-event="navigationDot_about"]')
    NAV_DOT_MIA = (By.CSS_SELECTOR, 'div[data-event="navigationDot_mia"]')
    NAV_DOT_BENEFITS = (By.CSS_SELECTOR, 'div[data-event="navigationDot_benefits"]')
    BENEFITS_CONNECT_BTN = (By.CSS_SELECTOR, 'a[data-event="conv_connect-benefits"]')
    TARIFF_CARD_BLACK = (By.CSS_SELECTOR, 'a[href="/tariff/black"]')
    SIMS_QUANTITY_BTNS = (By.CSS_SELECTOR, 'li[class="sim-number-selector__item"]')


class ToBusinessPageLocators:
    """Класс переменных для определения локаторов элементов страницы "https://msk.tele2.ru/business"""

    POPMECHANIC_SUBMIT_BTN = (By.CSS_SELECTOR, 'button[class="popmechanic-submit popmechanic-submit-close"]')
    FOR_BUSINESS_BTN = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div['
                                  '1]/div/div/div/div/header/section[1]/ul/li[2]/a')


class OffersPageLocators:
    """Класс переменных для определения локаторов элементов страницы "https://msk.tele2.ru/bolshe/offers"""

    POPMECHANIC_SUBMIT_BTN = (By.CSS_SELECTOR, 'button[class="popmechanic-submit popmechanic-submit-close"]')
    DISCOUNT_CASHBACK = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div['
                                   '1]/div/div/div/div/header/section[1]/ul/li[3]/a')
