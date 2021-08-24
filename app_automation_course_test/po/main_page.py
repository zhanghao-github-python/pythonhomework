# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/8/23
Project ： PyCharm
File  : main_page
E-mail: zh13997821732@163.com


================================================================================

"""
# 主页
from selenium.webdriver.common.by import By


from app_automation_course_test.po.base_page import BasePage

from app_automation_course_test.po.address_list_page import AddressPage

class MainPage(BasePage):

    def click_address_list(self):
        # 在主页点击通讯录

        self.find(By.XPATH,"//*[@text='通讯录']").click()

        return AddressPage(self.driver)