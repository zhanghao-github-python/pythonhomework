# =================conding: utf-8
"""
================================================================================

Author : Administrator
Created  on : 2021/6/30
Project ： PyCharm
File  : send_money.py
E-mail: zh13997821732@163.com


================================================================================

"""
from python_parctice.python_pop import money


def send_money():
    money.get_salary = True
    money.get_salary_status = money.get_salary
    print(f"当前是否发工资状态为:{money.get_salary_status}")
    print('工资到账，好开心！')


# send_money()
