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

    def find_by_css(self,css):
        return  self.driver.find_element_by_css_selector(css)
        # 封装退出浏览器方法
    def quit_browser(self):
        return self.driver.quit()

        # 封装获取随机邮箱
    def get_random_email(self):
        email_num = ''
        for i in range(8):
            num = random.randint(0, 9)
            s = str(random.choice([num]))
            email_num += s
        email = email_num + '@163.com'
        return email

        # 封装获取随机账号
    def get_random_number(self):
        num1 = ''
        # 预置12位数的账号
        for i in range(12):
            # 取12个数字并拼接
            num = (random.randint(0, 9))
            s = str(random.choice([num]))
            num1 += s
        return num1

        # 封装获取随机姓名
    def get_random_account(self):
        account = ""
        # 生成随机的8位数，8次循环
        for i in range(8):
            # 从0到9 中随便取整数
            num = random.randint(0, 9)
            # num = chr(random.randint(48,57))  # ASCII表示数字
            letter = chr(random.randint(97, 122))  # 取小写字母
            Letter = chr(random.randint(65, 90))  # 取大写字母
            s = str(random.choice([num, letter, Letter]))  # 从三种中随机取数据
            account += s
        accountzh = account + 'zh'
        return accountzh
        # 封装获取随机部门名称

    def get_department_name(self):
        first_name = ["王", "李", "张", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "上官", "钟", "常"]
        name2 = random.choice(first_name)
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xfe)
        val = f'{head:x} {body:x}'
        str1 = name2 + (bytes.fromhex(val).decode('gb2312')) + '部门'
        return str1
