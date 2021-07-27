# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/7/10
Project ： PyCharm
File  : test_calcul_yml
E-mail: zh13997821732@163.com


================================================================================

"""
import allure
import pytest
import yaml

from test_pytest.pythoncode import calculate
import logging

log = logging.getLogger()


def get_datas():
    # 打开yml文件 这种表示方式防止数据中有中文存在乱码情况
    with open('../../datas/calcul.yml', "r", encoding="utf-8") as f:
        # 读取yml文件中的内容
        data = yaml.safe_load(f)
    return data


# def test_get_datas():
#     print(get_datas())
@allure.feature('计算器模块')
class Test_calculate:
    # def setup_class(self):
    #     log.info('测试开始')
    #
    # def teardown_class(self):
    #     log.info('测试结束啦')

    def setup(self):
        log.info('开始计算')

    def teardown(self):
        log.info('结束计算')

    # 加法测试
    @allure.severity('CRITICAL')
    @allure.title('计算加法中的整数和为零情况')
    @allure.story('加法计算成功')
    @pytest.mark.parametrize("a, b, expect",
                             get_datas()['datas'],
                             ids=get_datas()['ids'])
    def test_add(self, get_calc_object, a, b, expect):
        with allure.step("第一步传入数据"):
            print("传数据")
        with allure.step("第二步比较数据"):
            print("比较数据")
        with allure.step("第三步给出结果"):
            print("测试结论")
        assert get_calc_object.add(a, b) == expect

    @allure.title('计算加法中浮点数相加情况')
    @allure.story('浮点数加法计算成功')
    @pytest.mark.parametrize("a, b, expect",
                             get_datas()['float'],
                             ids=get_datas()['ids_float'])
    def test_add_float(self, get_calc_object, a, b, expect):
        assert round(get_calc_object.add(a, b), 2) == expect

    @allure.title('计算加法中字符串和数字相加情况')
    @allure.story('相加失败，预期会抛异常')
    def test_add_error(self,get_calc_object):
        with pytest.raises(TypeError):
            result = 'a' + 1

    # 除法测试
    @allure.title('计算除法中正数、负数相除情况、被除数为0')
    @allure.story('除法计算成功')
    @pytest.mark.parametrize("a, b, expect",
                             get_datas()['div'],
                             ids=get_datas()['ids_div'])
    def test_division(self, a, get_calc_object, b, expect):
        assert get_calc_object.div(a, b) == expect
        # with pytest.raises(抛出的异常名称)： 抛出预期范围之内的异常，则用例通过
        # with pytest.raises(ZeroDivisionError):
        #     log.info('division by zero')
        # except ZeroDivisionError:
        #     log.info('division by zero')

    @allure.title('除数为0情况')
    @allure.story('相除失败，预期会抛异常')
    def test_division_error(self):
        with pytest.raises(ZeroDivisionError):
            result2 = 1 / 0
