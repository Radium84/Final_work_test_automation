from selenium.common.exceptions import NoSuchElementException
class BasePage():
        #Открываем страницу
        def open(self):
            self.browser.get(self.url)
        #Конструктор класса
        def __init__(self, browser, url, timeout=3):
            self.browser = browser
            self.url = url
            self.browser.implicitly_wait(timeout)
        #Переопределение сообщения об ошибке
        def is_element_present(self, how, what):
            try:
                self.browser.find_element(how, what)
            except (NoSuchElementException):
                return False
            return True
        
            
            