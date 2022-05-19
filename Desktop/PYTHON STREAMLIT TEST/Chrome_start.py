import time
from selenium import webdriver

driver_path = './chromedriver'
driver = webdriver.Chrome(driver_path)
driver.get('https://www.google.com/')

time.sleep(3)
driver.quit()