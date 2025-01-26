import allure
import data
from locators.order_page_locators  import OrderLocators
from locators.main_page_locators import MainLocators
from pages.base_page import BasePage
import random

class OrderPage(BasePage):
    @allure.step('Принимаем куки')
    def accept_cookie(self):
        return self.click_to_element(MainLocators.button_cookie)

    @allure.step('Нажимаем на кнопку заказа вверху')
    def order_button_up_click(self):
        self.click_to_element(MainLocators.order_button_up)

    @allure.step('Нажимаем на кнопку заказа внизу')
    def order_button_middle_click(self):
        self.click_to_element(MainLocators.order_button_middle)

    @allure.step('Заполняем имя')
    def set_name_input(self):
        self.add_text_to_element(OrderLocators.introduce_name, random.choice(data.User.names))

    @allure.step('Заполняем фамилию')
    def set_second_name(self):
        self.add_text_to_element(OrderLocators.introduce_second_name, random.choice(data.User.second_names))

    @allure.step('Заполняем адрес')
    def set_adress(self):
        self.add_text_to_element(OrderLocators.introduce_adress, random.choice(data.User.adress))

    @allure.step('Находим поле метро')
    def metro_field(self):
        self.find_element_with_wait(OrderLocators.select_metro).click()

    @allure.step('Выбираем станцию метро')
    def choose_station(self):
        self.find_element_with_wait(OrderLocators.metro_station_example_2).click()

    @allure.step('Заполняем телефон')
    def set_telephone(self):
        self.add_text_to_element(OrderLocators.introduce_number, random.choice(data.User.telephone))

    @allure.step('Нажимаем Далее')
    def press_next(self):
        self.click_to_element(OrderLocators.button_next)


    @allure.step('Находим поле "Когда привезти самокат"')
    def start_rent_date(self):
        self.click_to_element(OrderLocators.choose_date)

    @allure.step('Заполняем поле "Когда привезти самокат"')
    def set_start_rent_date(self):
        self.add_text_to_element(OrderLocators.choose_date, data.User.date)

    @allure.step('Заполняем поле "*Срок аренды"')
    def set_rent_time(self):
        self.click_to_element(OrderLocators.introduce_rent_time)
        self.click_to_element(OrderLocators.select_rent_time)

    @allure.step('Выбираем цвет самоката')
    def set_colour(self):
        self.click_to_element(OrderLocators.select_colour)

    @allure.step('Заполняем поле комментария')
    def set_comment(self):
        self.add_text_to_element(OrderLocators.introduce_comment, random.choice(data.User.comment))

    @allure.step('Нажимаем кнопки "Заказать" и "Да"')
    def press_order(self):
        self.click_to_element(OrderLocators.button_order_in_order)
        self.find_element_with_wait(OrderLocators.button_yes).click()

    @allure.step('Проверка наличия окна "Заказ оформлен"')
    def find_confirmation_table(self):
        self.find_element_with_wait(OrderLocators.confirmation_table)
        return True