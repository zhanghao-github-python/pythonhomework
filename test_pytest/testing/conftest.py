# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/7/11
Project ： PyCharm
File  : coftest
E-mail: zh13997821732@163.com


================================================================================

"""
import pytest
import logging

import yaml

log = logging.getLogger()

# scope='module',autouse='ture'

# def get_datas():
#     # 打开yml文件 这种表示方式防止数据中有中文存在乱码情况
#     with open('../../datas/calcul.yml', "r", encoding="utf-8") as f:
#         # 读取yml文件中的内容
#         data = yaml.safe_load(f)
#     return data

from test_pytest.pythoncode import calculate


@pytest.fixture(scope='function')
def get_calc_object():
    # setup
    logging.info("开始测试")
    calc = calculate.Calculator()
    yield calc
    # teardown
    logging.info("结束测试")


def pytest_collection_modifyitems(session, config, items: list):
    # print(items)
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
