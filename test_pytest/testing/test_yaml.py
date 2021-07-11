# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/7/10
Project ： PyCharm
File  : test_yaml
E-mail: zh13997821732@163.com


================================================================================

"""

import yaml

def test_datayaml():
    # 打开yml文件
    with open('../../datas/data.yml', "r", encoding="utf-8") as f:
        # 读取yml文件中的内容
        data = yaml.safe_load(f)
    print(data)
test_datayaml()

def test_calculyaml():
    # 打开yml文件
    with open('../../datas/calcul.yml', "r", encoding="utf-8") as f:
        # 读取yml文件中的内容
        data = yaml.safe_load(f)
    print(data)
test_calculyaml()