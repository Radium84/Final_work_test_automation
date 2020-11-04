from pages.product_page import ProductPage
from pages.busket_page import BusketPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
import pytest
import time
import faker

def test_guest_can_see_success_message(browser):
    
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_correct_book()
#Гость не видит успешное сообщение при пустой корзине

def test_guest_cant_see_success_message(browser):
    
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

#проверка на успешное добавление в корзину
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_buying_form()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.just_buy_a_book()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.just_buy_a_book()
    
    page.should_not_be_disappeared_message()

#Гость должен видеть ссылку на логин
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.need_review    
#Гость должен видеть ссылку на логин и может кликнуть по ней
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
@pytest.mark.need_review
#Проверяем состояние корзины, ее пустоту cо страницы товара
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_top_busket_page()
    busket_page = BusketPage(browser, browser.current_url)
    busket_page.should_not_be_goods()
    busket_page.should_be_empty_text()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        login_link= "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser,login_link)
        page.open()
        f = faker.Faker()
        email = f.email()
        password = str(time.time())
        page.register_new_user(email=email,password=password)
        page.should_be_authorized_user()
        
        
    
    #Пользователь не видит успешное сообщение при пустой корзине
    def test_user_cant_see_success_message(self,browser):
        link = " http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    #Юзер может добавить товар в корзину
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        link = " http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_buying_form()

