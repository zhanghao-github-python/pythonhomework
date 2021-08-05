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


class Test_Po:
    def setup(self):
        # 实例化MainPage类
        self.main_page = MainPage()
    def test_add_member(self):
        self.main_page.goto_add_member().add_member()
        sleep(3)
        add_success = self.main_page.find_by_id('js_tips')
        if add_success:
            print("添加成功")
        else:
            print("添加失败")
    def test_add_department(self):
        self.main_page.goto_address_list().add_department()
        sleep(3)
        add_department_success= self.main_page.find_by_id('js_tips')
        if add_department_success:
            print('添加部门成功')
        else:
            print('添加部门失败')
