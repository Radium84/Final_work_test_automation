from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        #Запускаем все три метода класса для проверки страницы
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Реализация проверки на корректный урл адресс
        assert "login" in self.browser.current_url, "Can't find login page"

    def should_be_login_form(self):
        # Реализуется проверка наличия формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # Реализуется проверка наличия формы регистрации
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Regestration form is not presented"

    def register_new_user(self, email, password):
        (self.browser.find_element(*LoginPageLocators.REG_EMAIL)).send_keys(email)
       
        pass_field1 = self.browser.find_element(*LoginPageLocators.REG_PASS1)
        pass_field1.send_keys(password)
        pass_field2 = self.browser.find_element(*LoginPageLocators.REG_PASS2)
        pass_field2.send_keys(password)
        button_reg = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        button_reg.click()
                
    
        
        
