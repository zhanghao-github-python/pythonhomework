# =================conding: utf-8
"""
================================================================================

Author : Administrator
Created  on : 2021/6/30
Project ： PyCharm
File  : select_money
E-mail: zh13997821732@163.com


================================================================================

"""
import money

def select_money():
    if money.get_salary == True:
        money.save_money += 1000
        print("发工资了工资为:{}".format(money.save_money))
    else:
        money.save_money = 1000
        print("没发工资工资为:{}".format(money.save_money))





