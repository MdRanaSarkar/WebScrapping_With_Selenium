import unittest
import time
from selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path='D:\\SeleniumTestCode\\driver\\chromedriver.exe')
driver.get('https://www.google.com')
driver.get_screenshot_as_file("google"+".png")
driver.get('https://www.facebook.com')
driver.get_screenshot_as_file("facebook" + ".png")
driver.close()
driver.quit()



