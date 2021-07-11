# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/7/10
Project ： PyCharm
File  : test_fixture_yield
E-mail: zh13997821732@163.com


================================================================================

"""

def test_search():
    print('搜索')


def test_addcart():
    print('加购')


def test_order(login):
    print('下单')
    print(login)
