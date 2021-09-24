# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/9/22
Project ： PyCharm
File  : base_api
E-mail: zh13997821732@163.com


================================================================================

"""
import logging

import requests


class BaseApi:
    # 设置 loging
    fileHandler = logging.FileHandler(filename="../logs/apitest.log", encoding="utf-8")
    # 设置日志等级
    logging.getLogger().setLevel(0)
    # 设置日志内容格式
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    fileHandler.setFormatter(formatter)
    # 设置生效
    logging.getLogger().addHandler(fileHandler)

    def log_info(self, msg):
        """
        封装写日志的方法
        :param msg:要打印的日志信息
        :return:
        """
        return logging.info(msg)

    def send_api(self, req):
        """
        二次封装requests模块
        :param req:
        :return:
        """
        self.log_info("-------------请求体打印-------------")
        self.log_info(req)
        r = requests.request(**req)
        self.log_info("-------------打印返回体-----------")
        self.log_info(r.json())
        return r
