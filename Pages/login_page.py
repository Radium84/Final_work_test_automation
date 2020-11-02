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