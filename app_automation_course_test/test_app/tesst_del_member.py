# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/8/25
Project ： PyCharm
File  : tesst_del_member
E-mail: zh13997821732@163.com


================================================================================

"""
from time import sleep

from selenium.webdriver.common.by import By

from app_automation_course_test.po.app import App
from app_automation_course_test.utils.get_datas import GetData


class TestDelMember:
    def setup_class(self):
        self.app = App()

    def setup(self):
        # 启动app
        self.main = self.app.start().goto_main()
        # 初始化Faker相关数据
        self.data = GetData()

    def teardown(self):
        self.app.stop()
    def test_delete_member(self):
        self.name = self.data.get_name()
        self.number = self.data.get_random_number()
        self.email = self.data.get_email()
        a = self.main.click_address_list().click_add_member().add_member().editor_member\
            (self.name, self.number,self.email).click_back().click_member(f"{self.name}")\
            .click_personnal_information().click_edit_member().delete_member()
        sleep(2)

        try:
            b = a.find(By.XPATH, f'//*[contains(@text,f"{self.name}")]')

        except Exception as f:
            print('删除成功')


