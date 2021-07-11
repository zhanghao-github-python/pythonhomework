# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/7/7
Project ： PyCharm
File  : test_1
E-mail: zh13997821732@163.com


================================================================================

"""
import allure
import pytest
from test_pytest.pythoncode import calculate
import logging

log = logging.getLogger()

@allure.feature('计算器')
class Test_calculate:
    def setup_class(self):
        log.info('测试开始')

    def teardown_class(self):
        log.info('测试结束啦')

    def setup(self):
        self.calculate = calculate.Calculator()
        log.info('开始计算')

    def teardown(self):
        log.info('结束计算')

    # 加法测试
    @pytest.mark.parametrize("a, b, expect",
                             [[1, 2, 3], [3000, 4000, 7000], [-1, -2, -3], [0.5, 0.7, 1.2], [-1, 1, 0]],
                             ids=['int', 'bignum', 'minus', "float", 'zero'])
    def test_add(self, a, b, expect):
        assert self.calculate.add(a, b) == expect

    # 除法测试

    @pytest.mark.parametrize("a, b, expect",
                             [[2, 2, 1], [4000, 1000, 4], [-1, -2, 0.5], [0.5, 0.1, 5], [-1, 0, -1]],
                             ids=['int', 'bignum', 'minus', "float", 'zero'])
    def test_division(self, a, b, expect):

        try:
            assert self.calculate.div(a, b) == expect
        except ZeroDivisionError:
            log.info('division by zero')
