# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/9/23
Project ： PyCharm
File  : utils
E-mail: zh13997821732@163.com


================================================================================

"""

import yaml
from faker import Faker
from jsonpath import jsonpath


class Utils:
    def __init__(self):
        self.faker = Faker("zh-CN")  # 实例化Faker函数
    @classmethod
    def get_datas(cls, filepath):
        """
        获取yaml里的数据并返回
        :param filepath: 文件路径
        :return:
        """
        # 打开yml文件 这种表示方式防止数据中有中文存在乱码情况
        with open(filepath, "r", encoding="utf-8") as f:
            # 读取yml文件中的内容
            datas = yaml.safe_load(f)
        return datas

    @classmethod
    def base_jsonpath(cls, obj, json_expr):
        """
        封装jsonpath
        :param obj:响应体返回的json()
        :param json_expr: jsonpath表达式
        :return:
        """
        return jsonpath(obj, json_expr)


    def get_name(self):
        return self.faker.name()  # 姓名


    def get_random_tagname(self):
        a = self.faker.name()
        return  self.faker.name()+'标签'

    def get_email(self):
        return self.faker.company_email()  # 随机邮箱

    def get_random_number(self):
        return self.faker.random_int(100000000, 1000000000)  # 随机的9位数

