# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/8/23
Project ： PyCharm
File  : edit_member_page
E-mail: zh13997821732@163.com


================================================================================

"""
# 编辑成员信息页面
from selenium.webdriver.common.by import By

from app_automation_course_test.po.base_page import BasePage


class EditorMember(BasePage):

    def editor_member(self, name, number, email):
        # 输入姓名
        self.find(By.XPATH, '//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys(name)
        # 输入账号
        self.find(By.XPATH, '//*[contains(@text,"帐号")]/../android.widget.EditText').send_keys(number)
        # 输入邮箱
        self.find(By.XPATH, '//*[contains(@text,"邮箱")]/../android.widget.EditText').send_keys(email)
        # 点击性别
        self.find(By.XPATH, '//*[contains(@text,"性别")]/../android.widget.RelativeLayout').click()
        # 选择性别为女
        self.find(By.XPATH, '//*[contains(@text,"女")]').click()
        # 滑动查找保存并点击
        self.swip_and_click("保存")
        from app_automation_course_test.po.add_member_page import AddMember
        # 返回添加成员页面
        return AddMember(self.driver)
    def delete_member(self):
        from app_automation_course_test.po.address_list_page import AddressPage
        # 点击删除成员
        self.swip_and_click("删除成员")
        # 点击确定删除
        self.find_and_click(By.XPATH,'//*[contains(@text,"确定")]')
        return AddressPage(self.driver)
