# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/8/5
Project ： PyCharm
File  : add_member_page
E-mail: zh13997821732@163.com


================================================================================

"""
from time import sleep

from selenium.webdriver import ActionChains, TouchActions

from web_automation_course_test.page.base_page import BasePage


class MemberPage(BasePage):

    def add_member(self):
        # email = self.get_random_email()  # 邮箱
        # number = self.get_random_number()  # 账号
        # accountzh = self.get_random_account()  # 姓名
        # 输入姓名
        self.find_by_id('username').send_keys(self.get_random_account())
        # 输入账号
        self.find_by_css('#memberAdd_acctid').send_keys(self.get_random_number())
        # 输入邮箱
        self.find_by_xpath('//input[@name="alias"]').send_keys(self.get_random_email())
        # 定位单选框'女'
        self.find_by_xpath('//form//label[2]/input').click()
        # 定位'上级'单选框
        self.find_by_xpath('//form//div/label/input[@class="ww_radio js_identity_stat"]').click()
        # 点击保存
        self.find_by_link_text('保存').click()
        sleep(1)

    def add_department(self):
        # 点击'+'
        self.find_by_xpath('//a[@class= "member_colLeft_top_addBtnWrap js_create_dropdown"]').click()
        # 点击添加部门
        self.find_by_link_text('添加部门').click()
        # 输入部门名称
        self.find_by_xpath('//form[@onsubmit="return false"]//input[@class="qui_inputText ww_inputText"]').send_keys(
            self.get_department_name())
        # 点击部门选择下拉框
        self.find_by_xpath('//a[@class= "qui_btn ww_btn ww_btn_Dropdown js_toggle_party_list"]').click()
        # 选择二级部门
        self.find_by_xpath('//form//a[@id="1688851092980127_anchor"]').click()
        # 实例化TouchActions ActionChains
        action = TouchActions(self.driver)
        action1 = ActionChains(self.driver)
        # 定义需要拖住不放的元素和需要移动的元素
        drag_element = self.find_by_xpath('//div[@class= "qui_dialog_head ww_dialog_head"]')
        # 向Y轴移动300距离
        action1.drag_and_drop_by_offset(drag_element, 0, 300).perform()
        # #点击取消
        # self.find_element_by_xpath('//a[@d_ck="cancel"]').click()
        # 点击确定
        self.find_by_xpath('//a[@d_ck="submit"]').click()
