# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/8/23
Project ： PyCharm
File  : address_list_page
E-mail: zh13997821732@163.com


================================================================================

"""
# 通讯录页面
from app_automation_course_test.po.add_member_page import AddMember
from app_automation_course_test.po.base_page import BasePage
from app_automation_course_test.po.personal_information_page import PersonalPage


class AddressPage(BasePage):
    def click_add_member(self):
        # 点击添加成员
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().'
        #                          'scrollable(true).instance(0)).'
        #                          'scrollIntoView(new UiSelector().'
        #                          'text("添加成员").instance(0));').click()

        self.swip_and_click("添加成员")
        return AddMember(self.driver)
    # 点击单个成员信息

    def click_member(self,name):

        self.swip_and_click(f'{name}')
        return PersonalPage(self.driver)
