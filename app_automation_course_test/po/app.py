# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/8/23
Project ： PyCharm
File  : test_app.py
E-mail: zh13997821732@163.com


================================================================================

"""
# 启动app
from appium import webdriver

from app_automation_course_test.po.base_page import BasePage
from app_automation_course_test.po.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            caps = {}
            # 设置app的平台（Android、iOS）
            caps["platformName"] = "Android"
            caps["deviceName"] = "wework"
            # 设置app的包名
            caps["appPackage"] = "com.tencent.wework"
            # 设置app启动页
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            # 不清空缓存启动app
            caps["noReset"] = "true"
            # 设置页面等待空闲状态的时间为0秒
            caps['settings[waitForIdleTimeout]'] = 10
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 设置隐式等待时间为10s
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()

        return self

    def stop(self):
        # 关闭app
        self.driver.quit()

    def restart(self):
        pass

    def goto_main(self):
        # app 主页
        return MainPage(self.driver)
