# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/8/5
Project ： PyCharm
File  : base_page
E-mail: zh13997821732@163.com


================================================================================

"""
import time
from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random

from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    url = "https://work.weixin.qq.com/"

    def __init__(self, driver: WebDriver = None):
        # 如果没有传递 driver ，说明是第一层调用，比如企业微信的官网
        if not driver:
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
        # 如果传递了 driver ,说明不是第一次调用，比如企业微信官网 -> 登陆界面
        else:
            self.driver = driver

    def find_by_id(self, id):
        """
        通过 id 进行查找
        :param id:
        :return:
        """
        return self.driver.find_element_by_id(id)
        # 封装xpath

    def find_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

        # 封装link_text方法

    def find_by_link_text(self, text):
        return self.driver.find_element_by_link_text(text)

    def find_by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

        # 封装退出浏览器方法

    def quit_browser(self):
        return self.driver.quit()
