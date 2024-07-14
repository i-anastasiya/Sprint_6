from selenium.webdriver.common.by import By


class BaseLocators:
    # Лого Яндекс
    LOGO_YANDEX = (By.CSS_SELECTOR, 'img[alt="Yandex"]')

    # Лого Самокат
    LOGO_SCOOTER = (By.CSS_SELECTOR, 'img[alt="Scooter"]')
