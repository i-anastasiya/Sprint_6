import pytest
from selenium import webdriver
from tests.constants import Constants


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.get(Constants.URL)
    yield browser
    browser.quit()


@pytest.fixture
def open_questions_about_importan(driver):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    return driver
