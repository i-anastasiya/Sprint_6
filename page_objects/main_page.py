import allure
from page_objects.base_page import BasePage
from locators.main_page_locators import MainLocators
from locators.base_page_locators import BaseLocators



class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Тап на лого Яндекс')
    def click_logo(self):
        self.driver.find_element(*BaseLocators.LOGO_YANDEX).click()

    @allure.step('Ждем открытие новой вкладки')
    def wait_new_window(self):
        self.window_handles = self.driver.window_handles
        self.driver.switch_to.window(self.window_handles[1])
    @allure.step('Сравниваем урл открытой страницы с ожидаемым')
    def make_sure_url(self):
        self.current_url = self.driver.current_url
        assert self.current_url == 'https://dzen.ru/?yredirect=true'

    @allure.step('Тап на кнопку Заказать вверху сайта')
    def tap_order_up(self):
        self.driver.find_element(*MainLocators.ORDER_BUTTON_UP).click()

    @allure.step('Тап на кнопку Заказать внизу сайта')
    def tap_order_down(self):
        self.driver.find_element(*MainLocators.ORDER_BUTTON_DOWN).click()

    def tap_logo(self):
        self.driver.find_element(*BaseLocators.LOGO_SCOOTER).click()

    @allure.step('Тапаем на вопрос в блоке Вопросы о важном')
    def tap_question(self, locator, index):
        selector, locator = locator
        locator = locator.format(index)
        self.wait_element((selector, locator))
        self.click((selector, locator))
        return self.wait_element((selector, locator)).get_attribute("id")

    @allure.step('Ищем ответ на вопрос в выпадающем списке')
    def find_answer(self, locator, index):
        selector, locator = locator
        locator = locator.format(index)
        element = self.wait_element((selector, locator))
        return element.text
