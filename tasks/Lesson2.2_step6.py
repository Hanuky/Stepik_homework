from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("window.scrollBy(0, 150);")

    # Считываем значение элемента X
    x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
    x = x_element.text
    y = calc(x)
    
    # Вставляем полученный результат в строку ответа
    input1 = browser.find_element_by_css_selector("input#answer.form-control")
    input1.send_keys(y)
    
    # Кликаем по чекбосу "I'm the robot"
    option1 = browser.find_element_by_css_selector("input#robotCheckbox.form-check-input")
    option1.click()
    
    # Выбираем радиобатон "Robots rule"
    option1 = browser.find_element_by_css_selector("input#robotsRule.form-check-input")
    option1.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()