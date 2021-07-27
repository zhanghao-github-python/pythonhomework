#!usr/bin/python
# -*- coding: UTF-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/7/15
Project ： PyCharm
File  : test_selenium
E-mail: zh13997821732@163.com


================================================================================

"""
import configparser
from time import sleep
import pytest
import  selenium
from selenium import webdriver
def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")

class TestWait:
    def setup(self):
        self.driver=webdriver.Firefox()
        self.driver.get('https://home.testing-studio.com/')
    def test_wait(self):
        sleep(3)
        print('hello')