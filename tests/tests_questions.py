import allure
import pytest
from locators.main_page_locators import MainLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestQuestionsPage:
    @pytest.mark.parametrize(
        'questions, answer',
        [
           ['Сколько это стоит? И как оплатить?', 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.']
        ]
    )

    @allure.step('open_1_question')
    def test_open_1_question(self, open_questions_about_importan, questions,  answer):
        #  тест проверяет тап на первый вопрос и открытие его ответа
        open_questions_about_importan.find_element(*MainLocators.QUESTION_1).click()
        questions_text = open_questions_about_importan.find_element(*MainLocators.QUESTION_1).text
        assert questions_text == questions
        answer_text = WebDriverWait(open_questions_about_importan, 3).until(EC.visibility_of_element_located
                                                                            ((MainLocators.ANSWER_1))).text
        assert answer_text == answer

    @pytest.mark.parametrize(
         'questions, answer',
        [
            ['Хочу сразу несколько самокатов! Так можно?', 'Пока что у нас так: один заказ — один самокат. '
             'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']
    ])

    @allure.step('open_2_question')
    def test_open_2_question(self, open_questions_about_importan, questions, answer):
        #  тест проверяет тап на второй вопрос и открытие его ответа
        open_questions_about_importan.find_element(*MainLocators.QUESTION_2).click()
        questions_text = open_questions_about_importan.find_element(*MainLocators.QUESTION_2).text
        assert questions_text == questions
        answer_text = WebDriverWait(open_questions_about_importan, 3).until(EC.visibility_of_element_located
                                                                            ((MainLocators.ANSWER_2))).text
        assert answer_text == answer

    @pytest.mark.parametrize(
        'questions, answer',
        [
            ['Как рассчитывается время аренды?', 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая'
            ' в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру.'
            ' Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']
        ])

    @allure.step('open_3_question')
    def test_open_3_question(self, open_questions_about_importan, questions, answer):
        #  тест проверяет тап на третий вопрос и открытие его ответа
        open_questions_about_importan.find_element(*MainLocators.QUESTION_3).click()
        questions_text = open_questions_about_importan.find_element(*MainLocators.QUESTION_3).text
        assert questions_text == questions
        answer_text = WebDriverWait(open_questions_about_importan, 3).until(EC.visibility_of_element_located
                                                                           ((MainLocators.ANSWER_3))).text
        assert answer_text == answer

    @pytest.mark.parametrize(
        'questions, answer',
        [
            ['Можно ли заказать самокат прямо на сегодня?', 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.']
        ])

    @allure.step('open_4_question')
    def test_open_4_question(self, open_questions_about_importan, questions, answer):
        #  тест проверяет тап на четвертый вопрос и открытие его ответа
        open_questions_about_importan.find_element(*MainLocators.QUESTION_4).click()
        questions_text = open_questions_about_importan.find_element(*MainLocators.QUESTION_4).text
        assert questions_text == questions
        answer_text = WebDriverWait(open_questions_about_importan, 3).until(EC.visibility_of_element_located
                                                                            ((MainLocators.ANSWER_4))).text
        assert answer_text == answer

    @pytest.mark.parametrize(
        'questions, answer',
        [
            ['Можно ли продлить заказ или вернуть самокат раньше?', 'Пока что нет! Но если что-то срочное — всегда'
                                                            ' можно позвонить в поддержку по красивому номеру 1010.']
        ])

    @allure.step('open_5_question')
    def test_open_5_question(self, open_questions_about_importan, questions, answer):
        #  тест проверяет тап на пятый вопрос и открытие его ответа
        open_questions_about_importan.find_element(*MainLocators.QUESTION_5).click()
        questions_text = open_questions_about_importan.find_element(*MainLocators.QUESTION_5).text
        assert questions_text == questions
        answer_text = WebDriverWait(open_questions_about_importan, 3).until(EC.visibility_of_element_located
                                                                            ((MainLocators.ANSWER_5))).text
        assert answer_text == answer

    @pytest.mark.parametrize(
        'questions, answer',
        [
            ['Вы привозите зарядку вместе с самокатом?', 'Самокат приезжает к вам с полной зарядкой. Этого хватает'
             ' на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']
        ])

    @allure.step('open_6_question')
    def test_open_6_question(self, open_questions_about_importan, questions, answer):
        #  тест проверяет тап на шестой вопрос и открытие его ответа
        open_questions_about_importan.find_element(*MainLocators.QUESTION_6).click()
        questions_text = open_questions_about_importan.find_element(*MainLocators.QUESTION_6).text
        assert questions_text == questions
        answer_text = WebDriverWait(open_questions_about_importan, 3).until(EC.visibility_of_element_located
                                                                            ((MainLocators.ANSWER_6))).text
        assert answer_text == answer

    @pytest.mark.parametrize(
        'questions, answer',
        [
            ['Можно ли отменить заказ?', 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже'
                                         ' не попросим. Все же свои.']
        ])

    @allure.step('open_7_question')
    def test_open_7_question(self, open_questions_about_importan, questions, answer):
        #  тест проверяет тап на седьмой вопрос и открытие его ответа
        open_questions_about_importan.find_element(*MainLocators.QUESTION_7).click()
        questions_text = open_questions_about_importan.find_element(*MainLocators.QUESTION_7).text
        assert questions_text == questions
        answer_text = WebDriverWait(open_questions_about_importan, 3).until(EC.visibility_of_element_located
                                                                            ((MainLocators.ANSWER_7))).text
        assert answer_text == answer


    @pytest.mark.parametrize(
        'questions, answer',
        [
            ['Я жизу за МКАДом, привезёте?', 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
        ])

    @allure.step('open_8_question')
    def test_open_8_question(self, open_questions_about_importan, questions, answer):
        #  тест проверяет тап на восьмой вопрос и открытие его ответа
        open_questions_about_importan.find_element(*MainLocators.QUESTION_8).click()
        questions_text = open_questions_about_importan.find_element(*MainLocators.QUESTION_8).text
        assert questions_text == questions
        answer_text = WebDriverWait(open_questions_about_importan, 3).until(EC.visibility_of_element_located
                                                                            ((MainLocators.ANSWER_8))).text
        assert answer_text == answer
