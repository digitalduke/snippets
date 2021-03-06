from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_value = browser.find_element(By.ID, "treasure")
answer = calc(x_value.get_attribute('valuex'))

answer_input = browser.find_element(By.ID, "answer")
answer_input.send_keys(answer)

checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()

radiobutton = browser.find_element(By.ID, "robotsRule")
radiobutton.click()

submit = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > div > button")
submit.click()
