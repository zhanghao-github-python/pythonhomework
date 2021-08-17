# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/8/6
Project ： PyCharm
File  : test_case
E-mail: zh13997821732@163.com


================================================================================

"""

from time import sleep

import pytest
import yaml

from web_automation_course_test.page.main_page import MainPage

from web_automation_course_test.page.tools import get_random_email, get_random_account, get_random_number, \
    get_department_name

def get_datas():
    # 打开yml文件 这种表示方式防止数据中有中文存在乱码情况
    with open('../datas/information.yml', "r", encoding="utf-8") as f:
        # 读取yml文件中的内容
        data = yaml.safe_load(f)
    return data
class Test_Po:
    def setup(self):
        # 实例化MainPage类
        self.main_page = MainPage()
        self.email = get_random_email()  # 获取邮箱
        self.accountzh = get_random_account()  # 获取姓名
        self.number = get_random_number()  # 账号
        self.departmentname = get_department_name()  # 获取部门

    # @pytest.mark.skip
    # @pytest.mark.parametrize("email1,accountzh,number", get_datas()['datas'])
    def test_add_member(self):
        # 进入添加成员界面添加成员
        self.main_page.goto_add_member().add_member(self.email, self.accountzh, self.number)
        sleep(3)
        # 获取邮箱元素
        getemail_success = self.main_page.find_by_xpath(f'//*[@title="{self.email}"]')
        # 用邮箱号码和获取的邮箱账号断言
        try:
            assert self.email == getemail_success.text
            print('添加成员成功')
        except Exception as f:
            print(f'添加失败了,错误信息是{f}')
    # @pytest.mark.skip
    def test_add_department(self):
        # 进入通讯录页面，添加部门
        self.main_page.goto_address_list().add_department(self.departmentname)
        sleep(3)
        # 获取部门名称
        getdepartment_name = self.main_page.find_by_xpath(
            f'//a[text()="{self.departmentname}"]')
        # 利用文本值和获取到的文本值做断言
        try:
            assert self.departmentname == getdepartment_name.text
            print('添加部门成功')
        except Exception as f:
            print(f'添加部门失败了,错误信息是{f}')
