import unittest
import time
from selenium import  webdriver

from selenium.webdriver.common.by import By
class autosuggessiontest(unittest.TestCase):

    def setUp(self):
        self.drive=webdriver.Chrome(executable_path='D:\\SeleniumTestCode\\driver\\chromedriver.exe')
        self.drive.maximize_window()
        self.drive.implicitly_wait(10)
    def test_autosuggetion(self):
        self.drive.get('https://www.goibibo.com/')
        self.drive.find_element(By.XPATH,"//input[@placeholder='From']").send_keys('Se')
        elements=self.drive.find_elements(By.XPATH,"//li[contains(@id,'react-autosuggest-1-suggestion')]//div[@class='mainTxt clearfix']//span")
        time.sleep(5)
        print(len(elements))
        for p in elements:
            print(p.text)
            if p.text=="Seattle, United States":
                print("record is found")
                p.click()
                break

        time.sleep(5)
        self.drive.find_element_by_id("gi_search_btn").click()
        current_url=self.drive.current_url
        print(current_url)
        #title
        current_title=self.drive.title
        print(current_title)
        titl="Goibibo - Best Travel Website. Book Hotels, Flights, Trains, Bus and Cabs with upto 50% off"


        self.assertEqual(current_title,titl)

    def tearDown(self):
        self.drive.close()
        self.drive.quit()

if __name__=='__main__':
    unittest.main()
