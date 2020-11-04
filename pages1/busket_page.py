from .base_page import BasePage
from .locators import BusketPageLocators

class BusketPage(BasePage):
    def should_not_be_goods(self):
        assert self.is_not_element_present(*BusketPageLocators.BUSKET_TITLE), \
       "Goods are presented, but should not be"
    
    def should_be_empty_text(self):
        text = (self.browser.find_element(*BusketPageLocators.EMPTY_BUSKET)).text
        assert text == "Your basket is empty. Continue shopping", "Busket should be empty"
