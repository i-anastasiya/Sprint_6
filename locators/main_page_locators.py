from selenium.webdriver.common.by import By


class MainLocators:

    # Вопрос в  блоке Вопросы о важном
    QUESTION = (By.ID, 'accordion__heading-{}')

    # Ответ в  блоке Вопросы о важном
    ANSWER = (By.ID, 'accordion__panel-{}')

    # Кнопка заказать вверху сайта
    ORDER_BUTTON_UP = (By.XPATH, ".//button[text()='Заказать']")

    # Кнопка заказать ввнизу сайта
    ORDER_BUTTON_DOWN = (By.XPATH, "//button[text()='Заказать']")

    # Заголовок сайта на главной
    TEXT_MAIN_PAGE = (By.CSS_SELECTOR, "div.Home_SubHeader__zwi_E")
