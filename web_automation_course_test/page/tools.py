# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/8/7
Project ： PyCharm
File  : tools
E-mail: zh13997821732@163.com


================================================================================

"""
import random


# 获取随机邮箱
def get_random_email():
    email_num = ''
    for i in range(8):
        num = random.randint(0, 9)
        s = str(random.choice([num]))
        email_num += s
    email = email_num + '@163.com'
    return email


# 封装获取随机账号
def get_random_number():
    num1 = ''
    # 预置12位数的账号
    for i in range(12):
        # 取12个数字并拼接
        num = (random.randint(0, 9))
        s = str(random.choice([num]))
        num1 += s
    return num1


# 获取随机姓名
def get_random_account():
    account = ""
    # 生成随机的8位数，8次循环
    for i in range(8):
        # 从0到9 中随便取整数
        num = random.randint(0, 9)
        # num = chr(random.randint(48,57))  # ASCII表示数字
        letter = chr(random.randint(97, 122))  # 取小写字母
        Letter = chr(random.randint(65, 90))  # 取大写字母
        s = str(random.choice([num, letter, Letter]))  # 从三种中随机取数据
        account += s
    accountzh = account + 'zh'
    return accountzh


# 获取随机的部门名称
def get_department_name():
    first_name = ["王", "李", "张", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "上官", "钟", "常"]
    name2 = random.choice(first_name)
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x} {body:x}'
    str1 = name2 + (bytes.fromhex(val).decode('gb2312')) + '部门'
    return str1
