from selenium.webdriver.common.by import By




class MainLocators:
    # Первый вопрос
    QUESTION_1 = (By.XPATH, ".//div[text()='Сколько это стоит? И как оплатить?']")

    # Второй вопрос
    QUESTION_2 = (By.XPATH, ".//div[text()='Хочу сразу несколько самокатов! Так можно?']")

    # Третий вопрос
    QUESTION_3 = (By.XPATH, ".//div[text()='Как рассчитывается время аренды?']")

    # Четвертый вопрос
    QUESTION_4 = (By.XPATH, ".//div[text()='Можно ли заказать самокат прямо на сегодня?']")

    # Пятый вопрос
    QUESTION_5 = (By.XPATH, ".//div[text()='Можно ли продлить заказ или вернуть самокат раньше?']")

    # Шестой вопрос
    QUESTION_6 = (By.XPATH, ".//div[text()='Вы привозите зарядку вместе с самокатом?']")

    # Седьмой вопрос
    QUESTION_7 = (By.XPATH, ".//div[text()='Можно ли отменить заказ?']")

    # Восьмой вопрос
    QUESTION_8 = (By.XPATH, ".//div[text()='Я жизу за МКАДом, привезёте?']")


    # Первый ответ
    ANSWER_1 = (By.ID, "accordion__panel-0")

    # Второй ответ
    ANSWER_2 = (By.ID, "accordion__panel-1")

    # Третий ответ
    ANSWER_3 = (By.ID, "accordion__panel-2")

    # Четвертый ответ
    ANSWER_4 = (By.ID, "accordion__panel-3")

    # Пятый ответ
    ANSWER_5 = (By.ID, "accordion__panel-4")

    # Шестой ответ
    ANSWER_6 = (By.ID, "accordion__panel-5")

    # Седьмой ответ
    ANSWER_7 = (By.ID, "accordion__panel-6")

    # Восьмой ответ
    ANSWER_8 = (By.ID, "accordion__panel-7")

    # Кнопка заказать вверху сайта
    ORDER_BUTTON_UP = (By.XPATH, ".//button[text()='Заказать']")

    # Кнопка заказать ввнизу сайта
    ORDER_BUTTON_DOWN = (By.XPATH, "//button[text()='Заказать']")

    # Заголовок сайта на главной
    TEXT_MAIN_PAGE = (By.CSS_SELECTOR, "div.Home_SubHeader__zwi_E")
