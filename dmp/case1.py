# encoding: utf-8
#!/usr/bin/python

# 变量用_var命名，地址不加_var ,xp表示xpath地址


import unittest
import time
import os
import random
from selenium import webdriver
from DMP.function import key_function
from DMP.function.home import HomePage



class Case1(unittest.TestCase):
#只调用一次 setUp用类方法setUpClass()。需要用 @classmethod 装饰器装饰起来
#普通方法setUp每次运行一个test 都调用一次setUp

    #类方法，第一个参数为类本身。类方法是只能由类名调用；静态方法可以由类名或对象名进行调用
    @classmethod
    def back_to_camp(cls):
        cls.dr.find_element_by_xpath('/html/body/div/div[1]/div/div[3]/ul/li[2]/p/a').click()

    @classmethod
    def setUpClass(self):
        print 'setUp'
        chromedriver=r"C:\Python27\chromedriver.exe"
        os.environ["webdriver.chrome.driver"]=chromedriver
        self.dr=webdriver.Chrome(chromedriver)
        # self.dr=webdriver.Chrome()
        key_function.login(self.dr)
        time.sleep(5)


    def test(self):
        home=HomePage()


        home.select_customer(self.dr,'cpic')
        time.sleep(2)

        home.menu_data_access(self.dr).click()
        home.submenu_data_overview(self.dr).click()


        time.sleep(3)

    @classmethod
    def tearDownClass(self):
        # self.assertEqual([],self.verificationErrors)
        print 'tearDown'
        self.dr.quit()



if __name__ == '__main__':
    unittest.main()
