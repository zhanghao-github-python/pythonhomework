# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/9/1
Project ： PyCharm
File  : test_get_token
E-mail: zh13997821732@163.com


================================================================================

"""
import requests


class Testtoken:
    def test_get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        corpid = "wwd9ca9cc9931d7db6"
        corpsecret = "TSEhoWQNmEu0CkBfgfHoyzCahAkhXgDN62eQjjXTVLI"
        r = requests.get(url=f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
        print(r.json())

    def test_get_token1(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        corpid = "wwd9ca9cc9931d7db6"
        corpsecret = "TSEhoWQNmEu0CkBfgfHoyzCahAkhXgDN62eQjjXTVLI"
        params = {"corpid": corpid, "corpsecret": corpsecret}
        r = requests.get(url=url, params=params)
        print(r.text)
