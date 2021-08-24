# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/8/24
Project ： PyCharm
File  : personal information_page
E-mail: zh13997821732@163.com


================================================================================

"""
from selenium.webdriver.common.by import By

from app_automation_course_test.po.base_page import BasePage
from app_automation_course_test.po.edit_member_page import EditorMember


class PersonalPage(BasePage):
    # 点击'...'按钮
    def click_personnal_information(self):
        self.find(By.XPATH, '//*[contains(@resource-id,"com.tencent.wework:id/hc9")]').click()
        return self

    # 点击'编辑成员'
    def click_edit_member(self):
        self.find(By.XPATH, '//*[contains(@text,"编辑成员")]').click()
        return EditorMember(self.driver)
