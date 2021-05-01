import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                 help="Choose language")
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser")                

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if  browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        options = FirefoxOptions()
        options.add_argument("-headless")
        browser = webdriver.Firefox(firefox_profile=fp, options=options)
        print("\n starting firefox browser for test..")
    else:
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language })
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(options=options)
        print("\n starting chorme browser for test..")
    yield browser
    print("\n quit browser..")
    time.sleep(5)
    browser.quit()