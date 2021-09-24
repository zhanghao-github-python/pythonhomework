# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/9/22
Project ： PyCharm
File  : test_wework1
E-mail: zh13997821732@163.com


================================================================================

"""
import requests

from api_automation_course_test.apis.base_api import BaseApi


class WeWork(BaseApi):
    def __init__(self, corpid, corpsecret):
        self.token = self.get_access_token(corpid, corpsecret)

    def get_access_token(self, corpid, corpsecret):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        # corpid = "wwd9ca9cc9931d7db6"
        # corpsecret = "TSEhoWQNmEu0CkBfgfHoyzCahAkhXgDN62eQjjXTVLI"
        # params = {"corpid": corpid, "corpsecret": corpsecret}
        req = {
            "method": "GET",
            "url": url
        }
        r = self.send_api(req)
        token = r.json()["access_token"]
        return token
