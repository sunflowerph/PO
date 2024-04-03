#coding=utf-8
import sys
sys.path.append('../basepase')


from homeBase import HomePage
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver

class LoginPage(HomePage):
    username_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/form/div[1]/div/div/input')
    password_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/form/div[2]/div/div/input')
    loginBtn_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/form/div[4]/div/button/span')
    succes_loc=(By.XPATH,'//*[@id="app"]/div/section/div/aside/div/div[1]/span')
    loginnull_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/form/div[1]/div/div[2]')
    pwnull_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/form/div[2]/div/div[2]')
    def login(self,username,password):
        self.dr.get(self.url)
        self.dr.find_element(*self.username_loc).send_keys(username)
        self.dr.find_element(*self.password_loc).send_keys(password)
        self.dr.find_element(*self.loginBtn_loc).click()
        sleep(3)
    def get_success(self):

        return self.dr.find_element(*self.succes_loc).text

    def get_loginnull(self):
        return self.dr.find_element(*self.loginnull_loc).text

    def get_pwnull(self):
        return self.dr.find_element(*self.pwnull_loc).text

# url='http://cmtest.project.agrisaas.com.cn/cm-jxs-test/#/login'
# dr=webdriver.Chrome()
# a=LoginPage(url,dr)
# a.login('phjxs','000000')
# print(a)