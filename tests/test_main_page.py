import time
import allure
import pytest
import data
from conftest import driver
from data import Answers
from pages.main_page import MainPage

class TestMainPage:
    @allure.title('Сравнение соответветствия ВОПРОС - ОТВЕТ')
    @allure.description('Подключена параметризация для теста')
    @pytest.mark.parametrize("question_id, expected_answer", Answers.answer_on_questions.items())
    def test_answer_on_question(self,driver, question_id, expected_answer):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        assert main_page.check_answer_for_question(question_id) == expected_answer

    @allure.title('Работа кнопки-логотипа "Самокат"')
    @allure.description('По нажатию на лого самоката попадаем на главную страницу')
    def test_button_scooter(self,driver):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.order_button_up_click()
        main_page.scooter_logo_button_click()
        assert main_page.get_current_url() == data.Urls.url

    @allure.title('Работа кнопки перехода на Дзен')
    @allure.description('По нажатию на лого Яндекс попадаем на Дзен')
    def test_button_dzen(self,driver):
        main_page = MainPage(driver)
        main_page.accept_cookie()
        main_page.dzen_logo_button_click()
        main_page.switch_window()
        time.sleep(2) #топорка, без которой не успевает...
        main_page.wait_for_url_changes()
        assert main_page.get_current_url() == data.Urls.url_dzen