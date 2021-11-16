from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
        
    x_1 = browser.find_element_by_css_selector("#num1")
    x_int = int(x_1.text)

    x_2 = browser.find_element_by_css_selector("#num2")
    x_int2 = int(x_2.text)
    
    def calc(x,y):
        return str(x+y)
    y = calc(x_int, x_int2)
    y_str = str(y)

    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(y_str)

    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
   

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
