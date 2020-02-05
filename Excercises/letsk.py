from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("http://google.com")
print(driver.title)
driver.implicitly_wait(10)
elem=driver.find_element_by_name("q")
elem.send_keys("Letskodeit")
elem.send_keys(Keys.RETURN)
print("executed")
time.sleep(5)
elem.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/div[1]/a')
elem.click()
elem=driver.find_element_by_xpath('//*[@id="navbar"]/div/div/div/ul/li[2]/a')
elem.click()

elem=driver.find_element(By.ID,"user_email")
elem.send_keys("remyavinod89@gmail.com")
elem.send_keys(Keys.RETURN)


elem=driver.find_element_by_xpath('//*[@id="user_password"]')
elem.send_keys("Pranchi2018$")
print("exicuted")
time.sleep(3)
elem=driver.find_element_by_name("commit")
elem.click()
