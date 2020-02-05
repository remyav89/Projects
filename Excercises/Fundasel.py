from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")

elem=driver.find_element_by_name("q")
elem.clear()
elem.send_keys("Brainbox Consulting")

elem.send_keys(Keys.RETURN)

elem.find_element_by_class_name("f1")
elem.click()