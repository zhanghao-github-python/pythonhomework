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


class WeWork:
    def __init__(self):
        self.token = self.get_access_token()

    def get_access_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        corpid = "wwd9ca9cc9931d7db6"
        corpsecret = "TSEhoWQNmEu0CkBfgfHoyzCahAkhXgDN62eQjjXTVLI"
        params = {"corpid": corpid, "corpsecret": corpsecret}
        r = requests.get(url=url, params=params)
        token = r.json()["access_token"]
        return token
