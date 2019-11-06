from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = " http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Достаем нужный атрибут
    gold_box = browser.find_element_by_css_selector("#treasure")
    number = gold_box.get_attribute("valuex")


    # Обчисление формулы
    x = number
    y = calc(x)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    # Выбор checkbox and radiobutton
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
