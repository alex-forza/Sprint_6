from selenium.webdriver.common.by import By
import data

class OrderLocators:
    introduce_name = [By.XPATH, './/input[@placeholder ="* Имя"]']
    introduce_second_name = [By.XPATH, './/input[@placeholder ="* Фамилия"]']
    introduce_adress = [By.XPATH, './/input[@placeholder ="* Адрес: куда привезти заказ"]']
    select_metro = [By.XPATH, '//input[@placeholder = "* Станция метро"]']
    metro_station_example_1 = [By.XPATH, f"//button[@value='{data.User.rnd_station}']"]
    metro_station_example_2 = [By.XPATH, "//button[@value='63']"]
    introduce_number = [By.XPATH, './/input[@placeholder ="* Телефон: на него позвонит курьер"]']
    button_next = [By.XPATH, '//button[text()="Далее"]']

    choose_date = [By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]']
    introduce_rent_time = By.XPATH, "//div[@class='Dropdown-control']"
    select_rent_time = [By.XPATH, "//div[@class='Dropdown-menu']//div[text()='двое суток']"]
    select_colour = [By.XPATH, f'//input[@id = "{data.User.rndcolour}"]']
    introduce_comment =[ By.XPATH, '//input[@placeholder ="Комментарий для курьера"]']
    button_back = [By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i" and text() = "Назад"]']
    button_order_in_order = [By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM" and text() = "Заказать"]']

    button_no = [By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i' and text() = 'нет']"]
    button_yes = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']"]

    confirmation_table = [By.XPATH, "//div[@class = 'Order_ModalHeader__3FDaJ']"]