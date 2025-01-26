import allure
from conftest import driver
from pages.order_page import OrderPage

class TestOrderPage:
    @allure.title('Создание заказа и его отслеживание')
    @allure.description('Заполнение формы создания заказа и его последующее отслеживание')
    def test_order_page(self,driver):
        order_page = OrderPage(driver)
        order_page.accept_cookie()
        order_page.order_button_up_click()
        order_page.set_name_input()
        order_page.set_second_name()
        order_page.set_adress()
        order_page.metro_field()
        order_page.choose_station()
        order_page.set_telephone()
        order_page.press_next()

        order_page.start_rent_date()
        order_page.set_start_rent_date()
        order_page.set_colour()
        order_page.set_rent_time()
        order_page.set_comment()
        order_page.press_order()

        assert order_page.find_confirmation_table() == True