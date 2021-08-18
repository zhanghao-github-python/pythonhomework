# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/8/17
Project ： PyCharm
File  : test_homework
E-mail: zh13997821732@163.com


================================================================================

"""
from time import sleep

from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web_automation_course_test.page.tools import get_random_number, get_random_account, get_random_email, \
    get_department_name
from faker import Faker


class TestDemo:
    def setup(self):
        desire_cap = {}
        desire_cap["platformName"] = "android"  # 平台
        desire_cap["deviceName"] = "127.0.0.1:7555"  # 设备名字
        desire_cap["appPackage"] = "com.tencent.wework"  # 包名
        desire_cap["appActivity"] = ".launch.WwMainActivity"  # 启动App的入口页面
        desire_cap["noReset"] = 'true'  # 不清除本地缓存
        # desire_cap["dontStopAppOnReset"] = 'true' # 停留在当前页面
        desire_cap["skipDeviceInitialization"] = 'true'
        # 设置页面等待空闲状态的时间为10秒
        desire_cap['settings[waitForIdleTimeout]'] = 10
        self.driver = webdriver.Remote("http://192.168.8.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def test_addmember(self):
        f = Faker(locale='zh_CN')  # 实例化Faker函数
        name = f.name()  # 姓名
        email = f.company_email()  # 随机邮箱
        number = f.random_int(100000000, 1000000000)  # 随机的9位数
        # 点击通讯录
        address_list = self.driver.find_element_by_xpath('//*[@text="通讯录"]')
        address_list.click()
        # 滑动查找账号并点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        # 点击手动输入添加
        self.driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
        # 输入姓名
        self.driver.find_element_by_xpath('//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys(name)
        # 输入账号
        self.driver.find_element_by_xpath('//*[contains(@text,"帐号")]/../android.widget.EditText').send_keys(number)
        # 输入邮箱
        self.driver.find_element_by_xpath('//*[contains(@text,"邮箱")]/../android.widget.EditText').send_keys(email)
        # 点击性别
        self.driver.find_element_by_xpath('//*[contains(@text,"性别")]/../android.widget.RelativeLayout').click()
        # 选择性别为女
        self.driver.find_element_by_xpath('//*[contains(@text,"女")]').click()
        # 滑动查找保存并点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("保存").instance(0));').click()
        # 强制等待1.5秒
        sleep(1.5)
        print(self.driver.page_source)  # 打印当前页面信息
        # 定位'添加成功'
        addmember_success = self.driver.find_element_by_xpath("//*[contains(@text,'添加成功')]").text
        try:
            assert addmember_success == '添加成功'
            print('添加成员用例成功了！')
        except Exception as f:
            print(f'添加成员用例失败错误信息是{f}')

        # # 点击返回
        # self.driver.find_element_by_xpath('//*[contains(@text,"添加成员")]/../../../../android.widget.TextView').click()
        # # 滑动查找账号文本值并点击
        # ele = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().'
        #                          'scrollable(true).instance(0)).'
        #                          'scrollIntoView(new UiSelector().'
        #                          f'text("{accountzh}").instance(0));').click()
        # # 点击后找到邮箱文本值
        # email_final = self.driver.find_element_by_xpath(f'//*[@text="{email}"]').text
        # # 文本值断言
        # try:
        #     assert  email == email_final
        #     print('添加成功')
        # except Exception as f:
        #     print(f'添加失败，错误信息是{f}')
