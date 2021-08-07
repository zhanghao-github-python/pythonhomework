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

from web_automation_course_test.page.main_page import MainPage

from web_automation_course_test.page.tools import get_random_email, get_random_account, get_random_number, \
    get_department_name


class Test_Po:
    def setup(self):
        # 实例化MainPage类
        self.main_page = MainPage()
        self.email = get_random_email()
        self.accountzh = get_random_account()
        self.number = get_random_number()
        self.departmentname = get_department_name()

    # @pytest.mark.skip
    def test_add_member(self):
        self.main_page.goto_add_member().add_member(self.email, self.accountzh, self.number)
        sleep(3)
        # 获取邮箱元素
        getemail_success = self.main_page.find_by_xpath(f'//*[@title="{self.email}"]')

        try:
            assert self.email == getemail_success.text
            print('添加成员成功')
        except Exception as f:
            print(f'添加失败了,错误信息是{f}')

    def test_add_department(self):
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
