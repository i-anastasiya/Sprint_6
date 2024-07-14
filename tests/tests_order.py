import allure
from faker import Faker
from locators.main_page_locators import MainLocators
from locators.order_page_locators import OrderLocators
from locators.about_rent_locators import AboutRentLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


faker = Faker()

class TestOrderPage:
    @allure.step('order_up')
    def test_order_up(self, driver):

        # тест на проверку оформления заказа, через верхнюю кнопку "Заказать"
        name = 'Иван'
        last_name = 'Иванов'
        address = 'ул. Красная площадь, д. 3'
        phone_number = '+7950000000'
        metro = 'Охотный ряд'
        driver.find_element(*MainLocators.ORDER_BUTTON_UP).click()
        # Ожидаем открытие экрана авторизации и проверяем, что именно он открылся
        tittle = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                      ((OrderLocators.ORDER_TITTLE))).text
        assert tittle == 'Для кого самокат'
        driver.find_element(*OrderLocators.INPUT_NAME).send_keys(name)
        driver.find_element(*OrderLocators.INPUT_LAST_NAME).send_keys(last_name)
        driver.find_element(*OrderLocators.INPUT_METRO_STATION).send_keys(metro)
        driver.find_element(*OrderLocators.METRO_STATION).click()
        driver.find_element(*OrderLocators.INPUT_ADDRESS).send_keys(address)
        driver.find_element(*OrderLocators.INPUT_NUMBER).send_keys(phone_number)
        driver.find_element(*OrderLocators.BUTTON_ONWARDS).click()
        # Проверяем, что открылся экран с информацией про аренду
        about_rent = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                ((AboutRentLocators.TEXT_ABOUT_RENT))).text
        assert about_rent == 'Про аренду'
        driver.find_element(*AboutRentLocators.INPUT_DATE).click()
        driver.find_element(*AboutRentLocators.DELIVERY_DATE).click()
        driver.find_element(*AboutRentLocators.INPUT_DATE_RENT).click()
        driver.find_element(*AboutRentLocators.RENTAL_PERIOD).click()
        driver.find_element(*AboutRentLocators.BUTTON_ORDER).click()
        # Проверяем окно подтверждения заказа
        confirm_order = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                    ((AboutRentLocators.TEXT_CONFIRM_ORDER))).text
        assert 'Хотите оформить заказ?' in confirm_order
        driver.find_element(*AboutRentLocators.BUTTON_YES).click()
        order_done = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                       ((AboutRentLocators.TEXT_ORDER_DONE))).text
        assert 'Заказ оформлен' in order_done


    @allure.step('order_down')
    def test_order_down(self, driver):

        # тест на проверку оформления заказа, через верхнюю кнопку "Заказать"
        name = 'Мария'
        last_name = 'Петрова'
        address = 'ул. Лесная, д. 23'
        phone_number = '+7950000001'
        metro = 'Охотный ряд'
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight / 0)")
        driver.find_element(*MainLocators.ORDER_BUTTON_DOWN).click()
        # Ожидаем открытие экрана авторизации и проверяем, что именно он открылся
        tittle = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                      ((OrderLocators.ORDER_TITTLE))).text
        assert tittle == 'Для кого самокат'
        driver.find_element(*OrderLocators.INPUT_NAME).send_keys(name)
        driver.find_element(*OrderLocators.INPUT_LAST_NAME).send_keys(last_name)
        driver.find_element(*OrderLocators.INPUT_METRO_STATION).send_keys(metro)
        driver.find_element(*OrderLocators.METRO_STATION).click()
        driver.find_element(*OrderLocators.INPUT_ADDRESS).send_keys(address)
        driver.find_element(*OrderLocators.INPUT_NUMBER).send_keys(phone_number)
        driver.find_element(*OrderLocators.BUTTON_ONWARDS).click()
        # Проверяем, что открылся экран с информацией про аренду
        about_rent = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                ((AboutRentLocators.TEXT_ABOUT_RENT))).text
        assert about_rent == 'Про аренду'
        driver.find_element(*AboutRentLocators.INPUT_DATE).click()
        driver.find_element(*AboutRentLocators.DELIVERY_DATE).click()
        driver.find_element(*AboutRentLocators.INPUT_DATE_RENT).click()
        driver.find_element(*AboutRentLocators.RENTAL_PERIOD).click()
        driver.find_element(*AboutRentLocators.BUTTON_ORDER).click()
        # Проверяем окно подтверждения заказа
        confirm_order = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                    ((AboutRentLocators.TEXT_CONFIRM_ORDER))).text
        assert 'Хотите оформить заказ?' in confirm_order
        driver.find_element(*AboutRentLocators.BUTTON_YES).click()
        order_done = WebDriverWait(driver, 3).until(EC.visibility_of_element_located
                                                       ((AboutRentLocators.TEXT_ORDER_DONE))).text
        assert 'Заказ оформлен' in order_done
