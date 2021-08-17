# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/8/8
Project ： PyCharm
File  : test_demo
E-mail: zh13997821732@163.com


================================================================================

"""
from time import sleep

import pytest
from appium import webdriver

# def test_demo():
#     desired_caps={}
#     desired_caps['platformName']='Android'
#     desired_caps['platformVersion']='6.0'
#     desired_caps['deviceName']='emulator-5554'
#     # com.android.settings/com.android.settings.Settings
#     desired_caps['appPackage']='com.android.settings'
#     desired_caps['appActivity']='com.android.settings.Settings'
#
#     driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
#     sleep(4)
#     print("启动【设置】应用")
#     driver.quit()
# def test_demo():
#     desire_cap = {
#       "platformName": "android",
#       "deviceName": "127.0.0.1:7555",
#       "appPackage": "com.xueqiu.android",
#       "appActivity": ".view.WelcomeActivityAlias",
#       "noReset":True
#     }
#     driver = webdriver.Remote("http://192.168.8.1:4723/wd/hub",desire_cap)
#     driver.implicitly_wait(10)
#     el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
#     # 点击搜索框
#     el1.click()
#     # 再次定位搜索框并输入‘阿里巴巴’
#     el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
#     el2.send_keys("阿里巴巴")
#     # 点击其中一个联想出来的‘阿里巴巴’
#     el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
#     el3.click()
from appium.webdriver.common.touch_action import TouchAction


class TestDemo:
    def setup(self):
        desire_cap = {}
        desire_cap["platformName"] = "android"  # 平台
        desire_cap["deviceName"] = "127.0.0.1:7555"  # 设备名字
        desire_cap["appPackage"] = "com.xueqiu.android"  # 包名
        desire_cap["appActivity"] = ".common.MainActivity"  # 被测页面
        desire_cap["noReset"] = 'true'  # 记住操作
        # desire_cap["dontStopAppOnReset"] = 'true' # 停留在当前页面
        desire_cap["skipDeviceInitialization"] = 'true'
        self.driver = webdriver.Remote("http://192.168.8.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)
    @pytest.mark.skip
    def test_currentprice(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # 点击搜索框
        el1.click()
        # 再次定位搜索框并输入‘阿里巴巴’
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("阿里巴巴")
        # 点击其中一个联想出来的‘阿里巴巴’
        el3 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and @text='阿里巴巴']")
        el3.click()
        current_price = self.driver.find_element_by_xpath('//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        print(f"09988当前股票的价格为：{current_price}")
        try:
            assert  float(current_price) < 200
            print('小于200')
        except Exception as f:
            print(f'股票价格大于200错误信息是{f}')
    def test_myinfo(self):
        """
        1.登录雪球
        2.点击我的，进入到个人信息页面
        3.点击登录，进入到登录页
        4.输入用户名，输入密码
        5.点击登录
        :return:
        """
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('13997821732')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('Zh123456.')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

# def test_demo1(self):
#     desire_cap = {}
#     desire_cap["platformName"] = "android"  # 平台
#     desire_cap["deviceName"] = "127.0.0.1:7555"  # 设备名字
#     desire_cap["appPackage"] = "com.xueqiu.android"  # 包名
#     desire_cap["appActivity"] = ".view.WelcomeActivityAlias"  # 被测页面
#     desire_cap["noReset"] = 'true'  # 记住操作
#     # desire_cap["dontStopAppOnReset"] = 'true'
#     desire_cap["skipDeviceInitialization"] = 'true'
#     driver = webdriver.Remote("http://192.168.8.1:4723/wd/hub", desire_cap)
#     driver.implicitly_wait(10)
#     el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
#     # 点击搜索框
#     el1.click()
#     # 再次定位搜索框并输入‘阿里巴巴’
#     el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
#     el2.send_keys("阿里巴巴")
#     # 点击其中一个联想出来的‘阿里巴巴’
#     el3 = driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and @text='阿里巴巴']")
#     el3.click()
#     # driver.back() # 回车
#     # sleep(3)
#     # driver.back()
#     sleep(3)
#     driver.quit() # 退出
######################## 手势滑动 #########################
# def test_touchaction(self):
#     """
#     手势密码解锁步骤：
#     1:按下第一个解锁图案，press方法
#     2:move_to方法移动到最后一个图案
#     3:调用release方法释放鼠标
#     4：调用perform方法展示存储的动作
#     :return:
#     """
#     action = TouchAction(self.driver)
#     window_rect = self.driver.get_window_rect()  # 获取窗口宽度和高度
#     width = window_rect['width']  # 宽
#     height = window_rect['height']  # 高
#     x1 = int(width / 2)  # X轴起点
#     y_start = int(height * 4 / 5)  # Y轴起点
#     y_end = int(height * 1 / 5)
#     action.press(x=x1, y=y_start).wait(200)
#     sleep(2)
#     action.move_to(x=x1, y=y_end).release().perform()
