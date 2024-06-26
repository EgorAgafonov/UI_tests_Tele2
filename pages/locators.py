from selenium.webdriver.common.by import By


class HomePageLocators:
    """Класс переменных для определения локаторов элементов страницы "https://msk.tele2.ru/home"""

    POPMECHANIC_MENU = (By.CSS_SELECTOR, 'div[class="popmechanic-title"]')
    POPMECHANIC_SUBMIT_BTN = (By.CSS_SELECTOR, 'button[class="popmechanic-submit popmechanic-submit-close"]')
    TWO_FACTOR_AUTH_CANCEL_BTN = (By.CSS_SELECTOR, 'a[class="cancel"]')
    LOGOUT_ACCOUNT_BTN = (By.CSS_SELECTOR, 'button[class="underscored-button"]')
    PRIVATE_CLIENTS_BTN = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div['
                                     '1]/div/div/div/div/header/section[1]/ul/li[1]/a')
    TIZER_VIDEO_BTN = (By.CSS_SELECTOR, 'span[class="btn tizer-video-announcement__link btn-white"]')
    NAV_DOT_ABOUT = (By.CSS_SELECTOR, 'div[data-event="navigationDot_about"]')
    NAV_DOT_MIA = (By.CSS_SELECTOR, 'div[data-event="navigationDot_mia"]')
    NAV_DOT_BENEFITS = (By.CSS_SELECTOR, 'div[data-event="navigationDot_benefits"]')
    BENEFITS_CONNECT_BTN = (By.CSS_SELECTOR, 'a[data-event="conv_connect-benefits"]')
    TARIFF_CARD_BLACK = (By.CSS_SELECTOR, 'a[href="/tariff/black"]')
    SIMS_QUANTITY_BTNS = (By.CSS_SELECTOR, 'li[class="sim-number-selector__item"]')
    ELEMENT_HOME_LOCATOR = (By.CSS_SELECTOR, 'h1[class="left h1 tariff-cards-container__title space-holder27"]')
    TARIFFS_CURRENT_PRICES = (By.CSS_SELECTOR, 'span[class="tariff-abonent-fee__current-price-value"]')

    # Блок переменных с локаторами формы авторизации зарегистрированного пользователя:
    ENTER_AUTH_BTN = (By.CSS_SELECTOR, 'a[class="gtm-new-navigation-login"]')
    AUTH_BY_SMS_BTN = (By.CSS_SELECTOR, 'button[class="unstyled-button filled-tabs__tab filled-tabs__tab--active"]')
    AUTH_BY_PASSWRD_BTN = (By.CSS_SELECTOR, 'button[class="unstyled-button filled-tabs__tab"]')
    PHONE_INPUT_FIELD = (By.CSS_SELECTOR, 'input[type="tel"]')
    PASSWORD_INPUT_FIELD = (By.ID, 'textField_password')
    ENTER_BY_PASSWRD_BTN = (By.CSS_SELECTOR, 'button[class="keycloak-login-form__button btn btn-black"]')
    CLOSE_AUTH_MENU_BTN = (By.CSS_SELECTOR, 'a[class="not-print-element close icon-close"]')
    FURTHER_BTN = (By.CSS_SELECTOR, 'button[class="keycloak-login-form__button btn btn-black"]')
    CODE_INPUT_FIELD = (By.CSS_SELECTOR, 'input[name="SMS"]')
    ENTER_PASSWRD_ERROR_MSSG = (By.CSS_SELECTOR, 'span[class="error-text"]')
    ENTER_PHONE_NUM_ERROR_MSSG = (By.CSS_SELECTOR, 'span[class="error-text"]')
    ACCOUNTS_AVATAR_DATA = (By.CSS_SELECTOR, 'span[class="br"]')


class ToBusinessPageLocators:
    """Класс переменных для определения локаторов элементов страницы "https://msk.tele2.ru/business"""

    POPMECHANIC_SUBMIT_BTN = (By.CSS_SELECTOR, 'button[class="popmechanic-submit popmechanic-submit-close"]')
    FOR_BUSINESS_BTN = (By.XPATH, '//*[@id="root"]//section[1]/ul/li[2]/a')
    SELECTOR_TITLE = (By.CSS_SELECTOR, 'h1[class=" h1"]')
    SELECTOR_PAYMENT_PERIODS = (By.CSS_SELECTOR, 'li[class="discount-selector__item"]')
    BUSINESS_TARIFFS_CURRENT_PRICES = (By.CSS_SELECTOR, 'span[class="tariff-card-price__value"]')
    VIP_NUMBERS_BANNER = (By.CSS_SELECTOR, 'div[class="numbers-sale-banner-b2b__animation"]')
    VIP_NUMBERS_CATALOG_BTN = (By.CSS_SELECTOR, 'a[class="numbers-sale-banner-b2b__redirect-link btn "]')
    VIP_PHONE_NUMBERS = (By.XPATH, '//*[@id="root"]//div/span/span')
    VIP_NUMBERS_RESULTS = (By.CSS_SELECTOR, 'div[class="phone-number-column"] > span > span')
    NUM_PRICE_0 = (By.XPATH, '//*[@id="root"]//ul/li[1]/span')
    NUM_PRICE_1000 = (By.XPATH, '//*[@id="root"]//ul/li[2]/span')
    NUM_PRICE_3000 = (By.XPATH, '//*[@id="root"]//ul/li[3]/span')
    NUM_PRICE_15000 = (By.XPATH, '//*[@id="root"]//ul/li[4]/span')
    VIP_NUM_SEARCH_FIELD = (By.ID, 'searchNumber')


class OffersPageLocators:
    """Класс переменных для определения локаторов элементов страницы "https://msk.tele2.ru/bolshe/offers"""

    POPMECHANIC_SUBMIT_BTN = (By.CSS_SELECTOR, 'button[class="popmechanic-submit popmechanic-submit-close"]')
    DISCOUNT_CASHBACK = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div['
                                   '1]/div/div/div/div/header/section[1]/ul/li[3]/a')




