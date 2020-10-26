import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
#Добавляем язык по умолчанию англ.
def pytest_addoption(parser):
    parser.addoption('--language', \
                     action='store', default="en",
                     help="Choose you language:ru,en, etc.")

#По заданию нам нужен только Хром
@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', \
                                    {'intl.accept_languages': language_name})
    browser = webdriver.Chrome(options=options)
#Добавляем задержку для удобства при проверке языка     
    yield browser
    print("\nquit browser..")
    time.sleep(7)
    browser.quit()
    
