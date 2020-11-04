from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")
    REG_EMAIL = (By.ID,"id_registration-email")
    REG_PASS1 = (By.ID,"id_registration-password1")
    REG_PASS2 = (By.ID,"id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR,'[value="Register"]')

class ProductPageLocators():
    BUSKET_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
    INV_FORM = (By.ID,"messages")
    INV_BOOK = (By.XPATH,'//div[@id="messages"]/div[1]/div/strong')
    INV_PRICE = (By.XPATH,'//div[@id="messages"]/div[3]/div/p/strong')
    BOOK = (By.CSS_SELECTOR, ".product_main h1")
    PRICE = (By.CSS_SELECTOR, ".product_main p")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUSKET_BUTTON1 = (By.XPATH,"//span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class BusketPageLocators():
    BUSKET_TITLE = (By.CSS_SELECTOR, "#content_inner .basket-title")
    EMPTY_BUSKET = (By.CSS_SELECTOR, '#content_inner p')
    
