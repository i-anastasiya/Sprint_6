import allure

from locators.order_page_locators import OrderLocators


class OrderPage:
    @allure.step('Вводим данные пользователя')
    def send_keys_input(self):
        name = 'Иван'
        last_name = 'Иванов'
        address = 'ул. Красная площадь, д. 3'
        phone_number = '+7950000000'
        metro = 'Охотный ряд'
        self.driver.find_element(*OrderLocators.BUTTON_ONWARDS).click()
        self.driver.find_element(*OrderLocators.INPUT_NAME).send_keys(name)
        self.driver.find_element(*OrderLocators.INPUT_LAST_NAME).send_keys(last_name)
        self.driver.find_element(*OrderLocators.INPUT_METRO_STATION).send_keys(metro)
        self.driver.find_element(*OrderLocators.METRO_STATION).click()
        self.driver.find_element(*OrderLocators.INPUT_ADDRESS).send_keys(address)
        self.driver.find_element(*OrderLocators.INPUT_NUMBER).send_keys(phone_number)
        self.driver.find_element(*OrderLocators.BUTTON_ONWARDS).click()
