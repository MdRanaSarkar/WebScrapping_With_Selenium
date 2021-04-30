import unittest
import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import Workbook
import  smtplib
from email.message import EmailMessage

class autosuggessiontest(unittest.TestCase):
    def setUp(self):
        self.drive=webdriver.Chrome(executable_path='D:\\SeleniumTestCode\\driver\\chromedriver.exe')
        self.drive.maximize_window()
        self.drive.implicitly_wait(10)

    def test_websrapping(self):
        self.drive.get('https://www.amazon.com/')
        self.drive.find_element(By.XPATH,"//input[contains(@id,'twotabsearchtextbox')]").send_keys('Samsung')
        time.sleep(5)
        self.drive.find_element(By.XPATH,"//input[contains(@value,'Go')]").click()
        time.sleep(5)
        self.drive.find_element(By.XPATH,"//span[text()='SAMSUNG']").click()
        product_title=self.drive.find_elements(By.XPATH,"//span[contains(@class,'a-size-medium a-color-base a-text-normal')]")
        product_price=self.drive.find_elements(By.XPATH,"//span[contains(@class,'a-price-whole')]")

        p_title=[]
        p_price=[]
        for t in product_title:
            print(t.text)
            p_title.append(t.text)
        for p in product_price:
            print(p.text)
            p_price.append(p.text)
        zipdat=zip(p_title,p_price)
        wb=Workbook()
        wb["Sheet"].title="Samsung Data"
        sh=wb.active
        sh.append(['Name','Price'])
        for s in list(zipdat):
            sh.append(s)
            print(s)
        wb.save("amazondata.xlsx")

        current_url=self.drive.current_url
        print(current_url)
        #title
        current_title=self.drive.title
        print(current_title)
        titl="Amazon.com : Samsung"


        self.assertEqual(current_title,titl)







    def tearDown(self):
        self.drive.close()
        self.drive.quit()

class MailClass:
    def Sendmail(self):
        msg=EmailMessage()
        msg['Subject']="Samsung data scrapping"
        msg['from']="Authorization Team"
        msg['to']="tech1503031@gmail.com"

        with open('email.txt') as myma:
            data=myma.read()
            msg.set_content(data)

        with open('amazondata.xlsx','rb') as f:
            file_d=f.read()
            print("File data in Binary",file_d)
            file_name=f.name
            print("File name",file_name)
            msg.add_attachment(file_d,maintype="application",subtype="xlsx",file_name=file_name)
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
            server.login("ranasarkar1503031@gmail.com","ranasarkar15@")
            server.send_message(msg)
        print("Email sent")

if __name__=='__main__':
    unittest.main()
    a=MailClass()
    a.Sendmail()
