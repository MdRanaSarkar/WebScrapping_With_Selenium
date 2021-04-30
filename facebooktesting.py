import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path='D:\\SeleniumTestCode\\driver\\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.facebook.com/')
driver.implicitly_wait(10)
driver.find_element_by_link_text('Create New Account').click()
time.sleep(10)
driver.find_element_by_name('firstname').send_keys("Shahnaj")
time.sleep(5)
bdate=driver.find_element_by_name('birthday_day')
bds=Select(bdate)
bds.select_by_index(3)
time.sleep(7)
driver.quit()