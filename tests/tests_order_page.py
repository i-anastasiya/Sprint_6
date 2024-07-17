import allure
from faker import Faker
from locators.order_page_locators import OrderLocators
from locators.about_rent_locators import AboutRentLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from page_objects.about_rent_page import AboutRentPage

faker = Faker()

class TestOrderPage:
    @allure.description('Проверяем оформление заказа, через верхнюю кнопку "Заказать"')
    def test_order_up(self, driver):
        self.driver = driver
        MainPage.tap_order_up(self)
        # Ожидаем открытие экрана авторизации и проверяем, что именно он открылся
        tittle = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                      ((OrderLocators.ORDER_TITTLE))).text
        assert tittle == 'Для кого самокат'
        OrderPage.send_keys_input(self)
        # Проверяем, что открылся экран с информацией про аренду
        about_rent = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                ((AboutRentLocators.TEXT_ABOUT_RENT))).text
        assert about_rent == 'Про аренду'
        AboutRentPage.send_keys_date(self)
        # Проверяем окно подтверждения заказа
        confirm_order = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                            ((AboutRentLocators.TEXT_CONFIRM_ORDER))).text
        assert 'Хотите оформить заказ?' in confirm_order
        AboutRentPage.tap_button_yes(self)
        order_done = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                         ((AboutRentLocators.TEXT_ORDER_DONE))).text
        assert 'Заказ оформлен' in order_done


    @allure.description('Проверяем оформление заказа, через нижнюю кнопку "Заказать"')
    def test_order_down(self, driver):
        self.driver = driver
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight / 0)")
        MainPage.tap_order_down(self)
        # Ожидаем открытие экрана авторизации и проверяем, что именно он открылся
        tittle = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                      ((OrderLocators.ORDER_TITTLE))).text
        assert tittle == 'Для кого самокат'
        OrderPage.send_keys_input(self)
        # Проверяем, что открылся экран с информацией про аренду
        about_rent = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                ((AboutRentLocators.TEXT_ABOUT_RENT))).text
        assert about_rent == 'Про аренду'
        AboutRentPage.send_keys_date(self)
        # Проверяем окно подтверждения заказа
        confirm_order = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                    ((AboutRentLocators.TEXT_CONFIRM_ORDER))).text
        assert 'Хотите оформить заказ?' in confirm_order
        AboutRentPage.tap_button_yes(self)
        order_done = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                       ((AboutRentLocators.TEXT_ORDER_DONE))).text
        assert 'Заказ оформлен' in order_done
