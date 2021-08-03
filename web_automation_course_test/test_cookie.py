# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/7/28
Project ： PyCharm
File  : test_cookie
E-mail: zh13997821732@163.com


================================================================================

"""
import pytest
import  time
import selenium
from selenium import webdriver
import yaml
from selenium.webdriver.chrome.options import Options


class TestLogin:
    # @pytest.mark.skip
    def test_get_cookie_login_add_department(self):
        #不使用复用浏览器的方式获取cookie
        driver = webdriver.Chrome()
        # 进入页面
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        # 等待15秒，这个过程需要把扫码动作完成
        time.sleep(15)
        # 获取cookie，注意，需要在登录之后再去获取cookie，否则，获取到的cookie也无法使用
        cookie_var = driver.get_cookies()
        print(cookie_var)
        # 把cookie存入一个可以持久存储的地方，不要因为程序结束，而cookie变量不能使用
        yaml.safe_dump(cookie_var, open("cookie.yaml", mode="w",encoding="utf-8"))
        time.sleep(2)
        # 第一步，拿到cookie数据
        cookie_var =yaml.safe_load(open("cookie.yaml", encoding="utf-8"))
        print(cookie_var)
        # 第二步，
        # 需要打开浏览器，输入网页再写入cookie！！！！！
        driver = webdriver.Chrome()
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 将cookie数据写入到浏览器中
        for cookie in cookie_var:
            # 因为add cookie只支持传入单个的字典，所以我们需要循环调用，植入cookie
            driver.add_cookie(cookie)
        time.sleep(5)
        # 需要刷新一下页面
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(5)
