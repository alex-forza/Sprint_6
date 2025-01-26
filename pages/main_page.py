import allure
from locators.main_page_locators import MainLocators
from locators.base_page_locators import BaseLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step('Принимаем куки')
    def accept_cookie(self):
        return self.click_to_element(MainLocators.button_cookie)

    @allure.step('Прокручиваем страницу до последнего вопроса')
    def scroll_for_question_block(self):
        last_question = self.find_element_with_wait(MainLocators.question_locator_for_scroll)
        return self.scroll_for_element(last_question)

    @allure.step('Клик на вопрос')
    def click_for_question (self, question_id):
        locator_question = self.format_locators(MainLocators.question_locator, question_id)
        self.scroll_for_question_block()
        self.click_to_element(locator_question)

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, question_id):
        locator_answer = self.format_locators(MainLocators.answer_locator, question_id)
        self.scroll_for_question_block()
        return self.get_text_from_element(locator_answer)

    @allure.step('Проверка ответа на вопрос')
    def check_answer_for_question(self, question_id):
        self.click_for_question(question_id)
        return self.get_answer_text(question_id)

    @allure.step('Нажимаем на кнопку Самокат')
    def scooter_logo_button_click(self):
        self.click_to_element(BaseLocators.button_scooter)

    @allure.step('Нажимаем на кнопку Дзен')
    def dzen_logo_button_click(self):
        self.click_to_element(BaseLocators.button_dzen)

    @allure.step('Нажимаем на кнопку заказа вверху')
    def order_button_up_click(self):
        self.click_to_element(MainLocators.order_button_up)

    @allure.step('Ожидаем смены урла')
    def wait_for_url_changes(self):
        self.wait_url_changes('https://qa-scooter.praktikum-services.ru/')

    @allure.step('Нажимаем на кнопку заказа внизу')
    def order_button_middle_click(self):
        self.click_to_element(MainLocators.order_button_middle)