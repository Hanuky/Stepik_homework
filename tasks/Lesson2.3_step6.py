from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем на первую кнопку
    button = browser.find_element_by_css_selector("button.trollface.btn")
    button.click()
 
    # Переход на вкладку редиректа
    new_window = browser.window_handles[1]   
    browser.switch_to.window(new_window)

    # Считываем значение элемента X решаем задачу
    x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
    x = x_element.text
    y = calc(x)
    
    # Вставляем полученный результат в строку ответа
    input1 = browser.find_element_by_css_selector("input#answer.form-control")
    input1.send_keys(y)

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