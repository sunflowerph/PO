#coding=utf-8
#基础类
from selenium.webdriver.support.wait import WebDriverWait #显式等待
from selenium.webdriver.support import expected_conditions as EC #判断元素是否存在

class HomePage(object):
    def __init__(self,url,dr):
        self.url=url
        self.dr=dr

    def find_element(self,*loc):
        try:
            WebDriverWait(self.dr,20).until(EC.visibility_of_element_located(*loc))
            return self.dr.find_element(*loc)
        except:
            print(loc+'元素未定位到')