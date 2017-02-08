# encoding: utf-8
#!/usr/bin/python

import time
import os
import shutil
import MySQLdb
from FE.conf import property
from nt import chdir
import getpass
import random
import urllib2
import  json
import types

def login(dr):

    print 'test_login \n'
    URL=''

    # chromedriver=r"C:\Python27\chromedriver.exe"
    # os.environ["webdriver.chrome.driver"]=chromedriver
    # dr=webdriver.Chrome(chromedriver)


    #登录信息
    username=''
    password=''
    token=''

    #登录
    dr.get(URL)
    dr.maximize_window()
    dr.find_element_by_id('id_username').send_keys(username)
    dr.find_element_by_id('id_password').send_keys(password)
    dr.find_element_by_id('id_rsa_token').send_keys(token)
    dr.find_element_by_class_name('loginButton').click()


    return dr
