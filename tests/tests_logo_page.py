import allure
from page_objects.main_page import MainPage
from locators.main_page_locators import MainLocators
from locators.order_page_locators import OrderLocators
from selenium.webdriver.support.wait import WebDriverWait
from tests.constants import Constants
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


class TestLogoPage:

    @allure.description('Проверяем тап на лого Яндекс')
    def test_logo_yandex(self, driver):
        self.driver = driver
        MainPage.click_logo(self)
        MainPage.wait_new_window(self)
        self.current_url = self.driver.current_url
        WebDriverWait(driver, 6).until(expected_conditions.url_contains('https://dzen.ru/'))
        url_new_page = driver.current_url
        assert url_new_page == Constants.dzen_url

    @allure.description('Проверяем тап на лого Скутер')
    def test_logo_scooter(self, driver):
        self.driver = driver
        MainPage.tap_order_up(self)
        # Ожидаем открытие экрана авторизации и проверяем, что именно он открылся
        tittle = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                ((OrderLocators.ORDER_TITTLE))).text
        assert tittle == 'Для кого самокат'
        MainPage.tap_logo(self)
        text_main = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                ((MainLocators.TEXT_MAIN_PAGE))).text
        assert 'Привезём его прямо к вашей двери' in text_main
