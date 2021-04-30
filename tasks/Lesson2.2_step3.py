from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем числа с страницы и производим вычисления
    num1 = browser.find_element_by_css_selector("span#num1.nowrap")
    num2 = browser.find_element_by_css_selector("span#num2.nowrap")
    sum_x = int(num1.text) + int(num2.text)
    
    # Открываем выпадающий список и выбираем правильное число
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(sum_x))

    # Нажимаем кнопку Submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()