import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path='D:\\SeleniumTestCode\\driver\\chromedriver.exe')
driver.maximize_window()
driver.get('http://teton.tforcehrms.com/admin')
#username=driver.find_element_by_name('iusername')
#username=driver.find_element(By.NAME,'iusername')
#using xpath
username=driver.find_element(By.XPATH,"//input[@id='iusername']")
ua=username.is_enabled()
ud=username.is_displayed()
username.clear()
ut=username.get_attribute('type')
print(ut)
ucss=username.value_of_css_property('font-size')
print(ucss)
time.sleep(5)
username.send_keys("Sarkar")
time.sleep(5)
pagetitle=driver.title
print(pagetitle)
assert 'TForce HRMS | Log in' in pagetitle
curl=driver.current_url
print(curl)
driver.quit()