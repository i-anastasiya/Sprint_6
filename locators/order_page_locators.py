from selenium.webdriver.common.by import By


class OrderLocators:
    # Заголовок на странице оформления заказа с текстом "Для кого самокат"
    ORDER_TITTLE = (By.XPATH, ".//div[text()='Для кого самокат']")

    # Инпут для ввода имени на экране заказа
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")

    # Инпут для ввода фамилии на экране заказа
    INPUT_LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")

    # Инпут для ввода адреса на экране заказа
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")

    # Инпут для ввода станции метро на экране заказа
    INPUT_METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")

    # Ячейка выбора станции метро в выпадающем списке
    METRO_STATION = (By.XPATH, "//div[text()='Охотный Ряд']")

    # Инпут для ввода номера телефона на экране заказа
    INPUT_NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Кнопка Далее на экарне авторизации
    BUTTON_ONWARDS = (By.XPATH, ".//button[text()='Далее']")
