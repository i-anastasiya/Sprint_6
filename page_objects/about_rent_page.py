import allure
from locators.about_rent_locators import AboutRentLocators

class AboutRentPage:
    @allure.step('Вводим данные по датам')
    def send_keys_date(self):
        self.driver.find_element(*AboutRentLocators.INPUT_DATE).click()
        self.driver.find_element(*AboutRentLocators.DELIVERY_DATE).click()
        self.driver.find_element(*AboutRentLocators.INPUT_DATE_RENT).click()
        self.driver.find_element(*AboutRentLocators.RENTAL_PERIOD).click()
        self.driver.find_element(*AboutRentLocators.BUTTON_ORDER).click()


    @allure.step('Тапаем на кнопку ДА')
    def tap_button_yes(self):
        self.driver.find_element(*AboutRentLocators.BUTTON_YES).click()
