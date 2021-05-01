import time
import math
import pytest
from selenium import webdriver

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    answer = str(math.log(int(time.time())))
    input1 = browser.find_element_by_css_selector("textarea.textarea")
    input1.send_keys(answer)
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    x = browser.find_element_by_css_selector(".smart-hints__hint")

    assert x.text == "Correct!", x.text