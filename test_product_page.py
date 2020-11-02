from pages.product_page import ProductPage
from pages.busket_page import BusketPage
import pytest
import time
#проверка на успешное добавление в корзину
#def test_guest_can_add_product_to_basket(browser):
#    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
#    page = ProductPage(browser, link)
#    page.open()
#    page.should_be_buying_form()
#def test_guest_can_see_success_message(browser):
    
 #   link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
 #   page = ProductPage(browser, link)
  #  page.open()
 #  page.should_be_correct_book()
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.just_buy_a_book()
    page.should_not_be_success_message()

@pytest.mark.skip    
def test_guest_cant_see_success_message(browser):
    
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.just_buy_a_book()
    
    page.should_not_be_disappeared_message()
@pytest.mark.skip
#Гость должен видеть ссылку на логин
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.skip    
#Гость должен видеть ссылку на логин и может кликнуть по ней
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

#Проверяем состояние корзины, ее пустоту cо страницы товара
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_top_busket_page()
    busket_page = BusketPage(browser, browser.current_url)
    busket_page.should_not_be_goods()
    busket_page.should_be_empty_text()

