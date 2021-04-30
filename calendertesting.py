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
        self.drive.get('http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html')
        time.sleep(5)
        self.drive.find_element(By.ID,"datepicker").click()
        cdata=self.drive.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//a")
        time.sleep(5)
        print(len(cdata))
        for p in cdata:
            print(p.text)
            if p.text=="24":
                print("record is found")
                p.click()
                break

        time.sleep(5)
        current_url=self.drive.current_url
        print(current_url)
        #title
        current_title=self.drive.title
        print(current_title)
        titl="Selenium Practise: How to handle calendar in Selenium Webdriver"
        self.assertEqual(current_title,titl)

    def tearDown(self):
        self.drive.close()
        self.drive.quit()

if __name__=='__main__':
    unittest.main()
