from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage): 
    
    def should_be_buying_form(self):
        busket = self.browser.find_element(*ProductPageLocators.BUSKET_BUTTON)
        busket.click()
        BasePage.solve_quiz_and_get_code(self)
        
        assert self.is_element_present(*ProductPageLocators.INV_FORM), "Form is not visible"
    def should_be_correct_book(self):
        busket = self.browser.find_element(*ProductPageLocators.BUSKET_BUTTON)
        busket.click()
        BasePage.solve_quiz_and_get_code(self)
        inv_name = (self.browser.find_element(*ProductPageLocators.INV_BOOK)).text
        inv_price =(self.browser.find_element(*ProductPageLocators.INV_PRICE)).text
        name =(self.browser.find_element(*ProductPageLocators.BOOK)).text
        price=(self.browser.find_element(*ProductPageLocators.PRICE)).text
        assert ((inv_name==name) and (inv_price == price)), "Wrong book"
        
    
