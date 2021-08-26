# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/8/23
Project ： PyCharm
File  : add_member_page
E-mail: zh13997821732@163.com


================================================================================

"""
# 添加成员页面
from selenium.webdriver.common.by import By

from app_automation_course_test.po.base_page import BasePage
from app_automation_course_test.po.edit_member_page import EditorMember


class AddMember(BasePage):
    def add_member(self):
        # 找到手动输入添加按钮并点击
        self.find_and_click(By.XPATH, "//*[@text='手动输入添加']")
        return EditorMember(self.driver)

    def find_toast(self):
        # 寻找toast弹框
        element = self.find(By.XPATH, "//*[@text='添加成功']")
        return element

    def click_back(self):
        from app_automation_course_test.po.address_list_page import AddressPage
        self.find_and_click(By.XPATH, '//*[contains(@text,"添加成员")]/../../../../android.widget.TextView')
        return AddressPage(self.driver)
