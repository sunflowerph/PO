#coding=utf-8

import sys
sys.path.append('../basepase')
sys.path.append('../page')
sys.path.append('../common')
# from homeBase import HomePage
# from loginpage import LoginPage
# from selenium import webdriver
import unittest
import time
from ownUnit import MyunitTests
from helper import Helper
from getImage import SaveImage
from HTMLTestRunner import HTMLTestRunner


class TestLogin(MyunitTests,Helper):

    def test_login(self):

        self.LoginPage.login(self.read_loginname(1),self.read_password(1))
        self.log('po-gjs:输入用户名和密码登录')
        self.assertEqual(self.LoginPage.get_success(),'经销商管理系统')
        self.log('登录成功后的断言')
        # SaveImage(self.dr,'login.png')
        self.log('截图')


    def test_loginnull(self):
        self.LoginPage.login(self.read_loginname(2), self.read_password(2))
        self.log('不输入密码')
        self.assertEqual(self.LoginPage.get_loginnull(), '请输入账号')
        self.log('断言')
        # SaveImage(self.dr,'loginnull.png')
        self.log('截图')

    def test_pwnull(self):
        self.LoginPage.login(self.read_loginname(3),self.read_password(3))
        self.assertEqual(self.LoginPage.get_pwnull(), '请输入密码')
        # SaveImage(self.dr,'pwnull.png')

if __name__ =="__main__":
    suit=unittest.TestSuite()
    alltests=unittest.defaultTestLoader.discover('.', pattern='test*.py') #查找所有的测试用例
    suit.addTests(alltests)
    filename = '../htmlResult/' + time.strftime('%Y_%m_%d_%H:%M:%S') + " report.html"
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp, title='我的测试报告', description='用例执行情况:')
    runner.run(suit)
    fp.close()
    Helper().send_mail(filename)


