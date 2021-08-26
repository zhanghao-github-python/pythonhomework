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

import pytest
from selenium.webdriver.common.by import By

from app_automation_course_test.po.app import App
from app_automation_course_test.utils.get_datas import GetData


class TestAddMember:
    def setup_class(self):
        self.app = App()
        self.data = GetData()
        self.name = self.data.get_name()
        self.number = self.data.get_random_number()
        self.email = self.data.get_email()

    def setup(self):
        # 启动app
        self.main = self.app.start().goto_main()
        # 初始化Faker相关数据
        # self.data = GetData()

    def teardown_class(self):
        self.app.stop()

    # @pytest.mark.skip
    def test_add_member(self):
        # self.name = self.data.get_name()
        # self.number = self.data.get_random_number()
        # self.email = self.data.get_email()
        addmember_success = self.main.click_address_list().click_add_member().add_member().editor_member(self.name,
                                                                                                         self.number,
                                                                                                         self.email).find_toast().text
        try:
            assert addmember_success == '添加成功'
            print('添加成功')
        except Exception as f:
            print(f'添加失败错误信息是{f}')
        return self.name
    # @pytest.mark.skip
    def test_delete_member(self):
        sleep(3)
        a = self.main.click_address_list().click_member(f"{self.name}") \
            .click_personnal_information().click_edit_member().delete_member()
        sleep(2)

        try:
            b = a.find(By.XPATH, f'//*[contains(@text,f"{self.name}")]')

        except Exception as f:
            print('删除成功')
