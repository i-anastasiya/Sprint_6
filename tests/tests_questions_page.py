import allure
import pytest
from total_information import TotalInformation
from locators.main_page_locators import MainLocators
from page_objects.main_page import MainPage

class TestQuestionsPage:

    @allure.title('Тест на получение соответствующих ответов после тапа на вопрос аккордеона.')
    @allure.description('В тесте проверяем что когда нажимаешь на стрелочку, открывается соответствующий текст.')
    @pytest.mark.parametrize(
        "index, text_answer",
        [
            (0, TotalInformation.text[0]),
            (1, TotalInformation.text[1]),
            (2, TotalInformation.text[2]),
            (3, TotalInformation.text[3]),
            (4, TotalInformation.text[4]),
            (5, TotalInformation.text[5]),
            (6, TotalInformation.text[6]),
            (7, TotalInformation.text[7])
        ])
    def test_answers(self, open_questions_about_importan, driver, index, text_answer):
        main_page = MainPage(driver)
        question = main_page.tap_question(MainLocators.QUESTION, index)
        result = main_page.find_answer(MainLocators.ANSWER, index)
        assert text_answer[question] == result
