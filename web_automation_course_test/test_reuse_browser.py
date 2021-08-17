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
from selenium.webdriver import TouchActions, ActionChains

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

    def get_department_name(self):
        first_name = ["王", "李", "张", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "上官", "钟", "常"]
        name2 = random.choice(first_name)
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xfe)
        val = f'{head:x} {body:x}'
        str1 = name2 + (bytes.fromhex(val).decode('gb2312')) + '部门'
        return str1

    # @pytest.mark.parametrize("name,account,email1", get_datas()['datas'])
    # def test_remote_chrome(self, name, account, email1):
    def test_remote_chrome(self):
        """
        复用浏览器到添加成员界面
        """
        departmentname = self.get_department_name()  # 部门
        email = self.get_random_email()  # 邮箱
        number = self.get_random_number()  # 账号
        accountzh = self.get_random_account()  # 姓名

        # 实例化 options
        option = Options()
        # 设定chrome debug 模式的一个地址
        # 设置opption的启动地址为127.0.0.1.9222
        option.debugger_address = "127.0.0.1:9222"
        # 实例化一个driver，driver 中设定了刚刚的debuggeraddress属性
        driver = webdriver.Chrome(options=option)
        driver.implicitly_wait(30)
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
            # 获取文本值和随机的账号名字做断言
            assert str(accountzh) == str(a.text)
            print('添加成功')
        except Exception as f:
            print(f'添加失败，错误信息是{f}')
        sleep(5)
        #                    添加部门操作
        driver.get('https://work.weixin.qq.com/wework_admin/frame#index')  # 返回首页
        # 点击添加成员
        driver.find_element_by_link_text('添加成员').click()
        # 点击'+'
        driver.find_element_by_xpath('//a[@class= "member_colLeft_top_addBtnWrap js_create_dropdown"]').click()
        # 点击添加部门
        driver.find_element_by_link_text('添加部门').click()
        # 输入部门名称
        driver.find_element_by_xpath(
            '//form[@onsubmit="return false"]//input[@class="qui_inputText ww_inputText"]').send_keys(
            f'{departmentname}')
        # 点击部门选择下拉框
        driver.find_element_by_xpath('//a[@class= "qui_btn ww_btn ww_btn_Dropdown js_toggle_party_list"]').click()
        # 点击所属部门
        driver.find_element_by_xpath('//form//a[@id="1688851092980127_anchor"]').click()
        # 实例化TouchActions ActionChains
        action = TouchActions(driver)
        action1 = ActionChains(driver)
        # 定义需要拖住不放的元素和需要移动的元素
        drag_element = driver.find_element_by_xpath('//div[@class= "qui_dialog_head ww_dialog_head"]')
        # 向Y轴移动300距离
        action1.drag_and_drop_by_offset(drag_element, 0, 300).perform()
        # #点击取消
        # driver.find_element_by_xpath('//a[@d_ck="cancel"]').click()
        # 点击确定
        driver.find_element_by_xpath('//a[@d_ck="submit"]').click()
        # 点击已经新增的部门
        driver.find_element_by_xpath(
            f'//a[text()="{departmentname}"]').click()
        b = driver.find_element_by_xpath(f'//span[text()="{departmentname}"]')
        try:
            # 获取文本值和随机的部门名字做断言
            assert str(departmentname) == (b.text)
            print('添加部门成功啦！！！')
        except Exception as f:
            print(f'添加部门失败了，错误信息是{f}')
        # if b :
        #     print('添加部门成功')
        # else:
        #     print('添加部门失败')
