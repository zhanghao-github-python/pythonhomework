# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/8/5
Project ： PyCharm
File  : main_page
E-mail: zh13997821732@163.com


================================================================================

"""
from web_automation_course_test.page.add_member_page import MemberPage
from web_automation_course_test.page.base_page import BasePage


class MainPage(BasePage):
    url = "https://work.weixin.qq.com/wework_admin/frame"  # 重写url：首页url

    def goto_add_member(self):
        # 点击添加成员
        self.driver.find_element_by_xpath("//*[@node-type='addmember']").click()
        return MemberPage(self.driver)
        # 进入添加通讯录页面

    def goto_address_list(self):
        # 点击通讯录
        self.find_by_css('#menu_contacts > span').click()
        return MemberPage(self.driver)
