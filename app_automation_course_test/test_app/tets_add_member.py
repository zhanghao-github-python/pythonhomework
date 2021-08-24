# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/8/24
Project ： PyCharm
File  : add_member
E-mail: zh13997821732@163.com


================================================================================

"""
from time import sleep

from app_automation_course_test.po.app import App
from app_automation_course_test.utils.get_datas import GetData


class TestAddMember:
    def setup_class(self):
        self.app = App()

    def setup(self):
        # 启动app
        self.main = self.app.start().goto_main()
        # 初始化Faker相关数据
        self.data = GetData()

    def teardown(self):
        self.app.stop()

    def test_add_member(self):
        self.name = self.data.get_name()
        self.number = self.data.get_random_number()
        self.email = self.data.get_email()
        addmember_success = self.main.click_address_list().click_add_member().add_member().editor_member(self.name, self.number, self.email).find_toast().text
        try:
            assert addmember_success == '添加成功'
            print('添加成功')
        except Exception as f:
            print(f'添加失败错误信息是{f}')


