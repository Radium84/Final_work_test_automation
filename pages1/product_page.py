from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage): 
    #просто покупаем книгу
    def just_buy_a_book(self):
        busket = self.browser.find_element(*ProductPageLocators.BUSKET_BUTTON)
        busket.click()
    #покупаем книгу, решаем задачку и проверяем наличие успеха   
    def should_be_buying_form(self):
        busket = self.browser.find_element(*ProductPageLocators.BUSKET_BUTTON)
        busket.click()
        BasePage.solve_quiz_and_get_code(self)
        assert self.is_element_present(*ProductPageLocators.INV_FORM), "Form is not visible"
    #ПОкупаем книгу, решаем задачку и сверяем цену с именем
    def should_be_correct_book(self):
        busket = self.browser.find_element(*ProductPageLocators.BUSKET_BUTTON)
        busket.click()
        BasePage.solve_quiz_and_get_code(self)
        inv_name = (self.browser.find_element(*ProductPageLocators.INV_BOOK)).text
        inv_price =(self.browser.find_element(*ProductPageLocators.INV_PRICE)).text
        name =(self.browser.find_element(*ProductPageLocators.BOOK)).text
        price=(self.browser.find_element(*ProductPageLocators.PRICE)).text
        assert ((inv_name==name) and (inv_price == price)), "Wrong book"
    #Сообщения об успехе не должно быть    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.INV_BOOK), \
       "Success message is presented, but should not be"
    #Ждем пока сообщение не исчезнет
    def should_not_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.INV_BOOK), \
               "Success message  was presented and then disappeared, but should not be"
