# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/7/28
Project ： PyCharm
File  : test_cookie
E-mail: zh13997821732@163.com


================================================================================

"""
import pytest
from time import sleep
import selenium
from selenium import webdriver
import yaml
from selenium.webdriver.chrome.options import Options


class TestCookie:
    def test_cookie(self):
        # 实例化Options
        option = Options()
        self.driver = webdriver.Chrome(options=option)
        option.debugger_address = "127.0.0.1:9222"
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        sleep(3)
