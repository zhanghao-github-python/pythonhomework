# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/9/21
Project ： PyCharm
File  : test_createdepartment
E-mail: zh13997821732@163.com


================================================================================

"""
import pytest
import requests
from app_automation_course_test.utils.get_datas import GetData


class TestWework:
    def setup_class(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        corpid = "wwd9ca9cc9931d7db6"
        corpsecret = "TSEhoWQNmEu0CkBfgfHoyzCahAkhXgDN62eQjjXTVLI"
        params = {"corpid": corpid, "corpsecret": corpsecret}
        self.r = requests.get(url=url, params=params)
        self.token = self.r.json()["access_token"]
        a = GetData()
        self.departmentname = a.get_department_name()
        self.id = a.get_random_number()
        print(self.id)
        print(self.departmentname)
        print(self.token)
        print(self.r.json())

    # @pytest.mark.skip
    @pytest.mark.parametrize(
        "departmentname,parentid,id",
        [["正常场景部门名称测试", 1, 23], ['', 1, 24]],
        ids=["正常场景部门测试", "异常场景部门测试"]
    )
    def test_createdepartment(self, departmentname, parentid, id):  # 创建部门
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
        params = {
            'access_token': self.token
        }
        data = {
            "name": departmentname,
            "parentid": parentid,
            "id": id
        }
        r = requests.post(url=url, params=params, json=data)
        print(r.json())
        # assert r.json()["errcode"] == 0
        try:
            assert r.json()["errcode"] == 0
            print('添加部门成功')
        except Exception:
            errmsg = r.json()['errmsg']
            print(f'添加部门失败错误信息是{errmsg}')
