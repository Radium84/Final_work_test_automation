from pages.main_page import MainPage
from pages.busket_page import BusketPage
from pages.login_page import LoginPage
import pytest

#Проверяем наличие ссылки на логин и возможность перехода
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    
    login_page.should_be_login_link()
            # выполняем метод страницы — переходим на страницу логина
#Проверяем наличие ссылки на логин
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
#Проверяем состояние корзины, ее пустоту с главной
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_top_busket_page()
    busket_page = BusketPage(browser, browser.current_url)
    busket_page.should_not_be_goods()
    busket_page.should_be_empty_text()
