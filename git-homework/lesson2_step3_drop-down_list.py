from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# def calc(x):
#     return str(num1) + str(num2)

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Обчисление формулы
    # answer = sum(map(int, [browser.find_element_by_id(name).text for name in ["num1", "num2"]]))
    num1_tag = browser.find_element_by_css_selector("#num1")
    num1 = num1_tag.text
    num2_tag = browser.find_element_by_css_selector("#num2")
    num2 = num2_tag.text
    answer = str(int(num1) + int(num2))

    # v1 - моё решение
    # # Создание селектора
    # x = "[value='" + answer + "']"
    # # Выбор drop-down
    # browser.find_element_by_tag_name("select").click()
    # browser.find_element_by_css_selector(x).click()

    # v2 - проще так
    select = Select(browser.find_element_by_css_selector("select"))
    select.select_by_value(str(answer))


    # Отправляем ответ
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Другой вариант
    # button = browser.find_element_by_tag_name(".btn").click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    # закрываем браузер после всех манипуляций
    browser.quit()
