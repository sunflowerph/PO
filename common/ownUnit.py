#coding=utf-8
import sys
sys.path.append('../basepase')
sys.path.append('../page')
from loginpage import LoginPage
from selenium import webdriver
import unittest
from time import sleep

class MyunitTests(unittest.TestCase):
    def setUp(self):
        self.url='http://cmtest.project.agrisaas.com.cn/cm-jxs-test/#/login'
        self.dr=webdriver.Chrome()
        self.LoginPage=LoginPage(self.url,self.dr)
    def tearDown(self):
        self.dr.quit()