from selenium.webdriver.common.by import By


class AboutRentLocators:
    # Заголовок на странице с информацией об аренде Про аренду"
    TEXT_ABOUT_RENT = (By.XPATH, "//div[text()='Про аренду']")

    # Инпут для ввода имени на экране заказа
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    # Инпут для ввода срока аренды
    INPUT_DATE_RENT = (By.XPATH, "//div[text()='* Срок аренды']")

    # Дата доставки
    DELIVERY_DATE = (By.XPATH, '//div[text()="24"]')

    # Срок аренды
    RENTAL_PERIOD = (By.XPATH, '//div[text()="двое суток"]')

    # Кнопка Заказать на экране информации про аренду
    BUTTON_ORDER = (By.XPATH, "//button[text()='Заказать']")

    # Заголовок подтверждения заказа
    TEXT_CONFIRM_ORDER = (By.XPATH, "//div[text()='Хотите оформить заказ?']")

    # Кнопка "Да" на экране подтверждения заказа
    BUTTON_YES = (By.XPATH, "//button[text()='Да']")

    # Уведомление об успешном заказе
    TEXT_ORDER_DONE = (By.CSS_SELECTOR, 'div.Order_ModalHeader__3FDaJ')
