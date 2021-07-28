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

import time
from time import sleep
import selenium
import yaml
from selenium import webdriver
import pytest

from selenium.webdriver.chrome.options import Options
import random


class Test_Add_Member:
    # @pytest.mark.skip
    def get_random_email(self):
        email_num = ''
        for i in range(8):
            num = random.randint(0, 9)
            s = str(random.choice([num]))
            email_num += s
        email = email_num + '@163.com'
        return email

    def get_random_number(self):
        num1 = ''
        #预置12位数的账号
        for i in range(12):
            #取12个数字并拼接
            num = (random.randint(0, 9))
            s = str(random.choice([num]))
            num1 += s
        return num1

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

    def test_remote_chrome(self):
        """
        复用浏览器到添加成员界面
        """
        email = self.get_random_email()
        number = self.get_random_number()
        accountzh = self.get_random_account()
        # 实例化 options
        option = Options()
        # 设定chrome debug 模式的一个地址
        # 设置opption的启动地址为127.0.0.1.9222
        option.debugger_address = "127.0.0.1:9222"
        # 实例化一个driver，driver 中设定了刚刚的debuggeraddress属性
        driver = webdriver.Chrome(options=option)
        # 获取添加成员的url
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        time.sleep(3)
        # 点击添加成员
        driver.find_element_by_link_text('添加成员').click()
        sleep(3)
        # 输入姓名
        driver.find_element_by_id('username').send_keys(accountzh)
        sleep(1)
        # 输入账号
        driver.find_element_by_css_selector('#memberAdd_acctid').send_keys(number)
        sleep(1)
        #输入邮箱
        driver.find_element_by_xpath('//input[@name="alias"]').send_keys(email)
        sleep(5)
        driver.find_element_by_xpath('//*[@id="js_contacts64"]/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
        sleep(3)
