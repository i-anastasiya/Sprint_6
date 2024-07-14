import time

import allure
from locators.main_page_locators import MainLocators
from locators.order_page_locators import OrderLocators
from locators.base_page_locators import BaseLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestLogoPage:

    @allure.step('logo_yandex')
    def test_logo_yandex(self, driver):
        # тест проверяет тап на лого Яндекс
        driver.find_element(*BaseLocators.LOGO_YANDEX).click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'

    @allure.step('logo_scooter')
    def test_logo_scooter(self, driver):
        driver.find_element(*MainLocators.ORDER_BUTTON_UP).click()
        # Ожидаем открытие экрана авторизации и проверяем, что именно он открылся
        tittle = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                ((OrderLocators.ORDER_TITTLE))).text
        assert tittle == 'Для кого самокат'
        driver.find_element(*BaseLocators.LOGO_SCOOTER).click()
        text_main = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                ((MainLocators.TEXT_MAIN_PAGE))).text
        assert 'Привезём его прямо к вашей двери' in text_main

