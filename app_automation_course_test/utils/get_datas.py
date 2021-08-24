# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/8/24
Project ： PyCharm
File  : get_datas
E-mail: zh13997821732@163.com


================================================================================

"""
from faker import Faker


class GetData:
    def __init__(self):
        self.faker = Faker("zh-CN")  # 实例化Faker函数

    def get_name(self):
        return self.faker.name()  # 姓名

    def get_email(self):
        return self.faker.company_email()  # 随机邮箱

    def get_random_number(self):
        return self.faker.random_int(100000000, 1000000000)  # 随机的9位数
