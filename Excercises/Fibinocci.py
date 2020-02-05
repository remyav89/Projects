from selenium import webdriver
from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())


driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()

driver.get('http://www.google.com')