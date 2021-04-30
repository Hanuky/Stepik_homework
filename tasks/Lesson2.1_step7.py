from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение элемента X из картинки забрав значение её атрибута
    treasure_value = browser.find_element_by_id("treasure")
    x = treasure_value.get_attribute("valuex")
    y = calc(x)
    
    # Вставляем полученный результат в строку ответа
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    # Кликаем по чекбосу "I'm the robot"
    option1 = browser.find_element_by_css_selector("input#robotCheckbox.check-input")
    option1.click()
    
    # Выбираем радиобатон "Robots rule"
    option1 = browser.find_element_by_css_selector("input#robotsRule.check-input")
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