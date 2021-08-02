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


def get_datas():
    # 打开yml文件 这种表示方式防止数据中有中文存在乱码情况
    with open('../datas/information.yml', "r", encoding="utf-8") as f:
        # 读取yml文件中的内容
        data = yaml.safe_load(f)
    return data


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
        # 预置12位数的账号
        for i in range(12):
            # 取12个数字并拼接
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

    # @pytest.mark.parametrize("name,account,email1", get_datas()['datas'])
    # def test_remote_chrome(self, name, account, email1):
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
        # driver.find_element_by_id('username').send_keys(name)
        sleep(1)
        # 输入账号
        driver.find_element_by_css_selector('#memberAdd_acctid').send_keys(number)
        # driver.find_element_by_css_selector('#memberAdd_acctid').send_keys(account)
        sleep(1)
        # 输入邮箱
        driver.find_element_by_xpath('//input[@name="alias"]').send_keys(email)
        # driver.find_element_by_xpath('//input[@name="alias"]').send_keys(email1)
        sleep(2)
        # 定位女
        driver.find_element_by_xpath('//form//label[2]/input').click()
        sleep(2)
        # 定位上级单选框
        driver.find_element_by_xpath('//form//div/label/input[@class="ww_radio js_identity_stat"]').click()
        sleep(2)
        driver.find_element_by_link_text('保存').click()
        sleep(3)
        a = driver.find_element_by_xpath(f'//span[text()="{accountzh}"]')
        try:

            assert str(accountzh) == str(a.text)
            print('添加成功')
        except Exception as f:
            print(f'添加失败，错误信息是{f}')
        sleep(5)
