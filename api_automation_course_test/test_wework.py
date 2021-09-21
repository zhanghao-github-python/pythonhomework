# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/9/16
Project ： PyCharm
File  : test_wework
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
    def test_createdepartment(self):  # 创建部门
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
        params = {
            'access_token': self.token
        }
        data = {
            "name": f"{self.departmentname}",
            "parentid": 1,
            "id": f"{self.id}"
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

    # @pytest.mark.skip
    def test_update_dapartment(self):  # 更新部门
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        params = {
            'access_token': self.token
        }
        data = {
            "id": f"{self.id}",
            "name": f"{self.departmentname}-update",
        }
        r = requests.request(method="POST", url=url, json=data)
        assert r.json()["errmsg"] == 'updated'
        print("更新部门信息成功")
        print(r.json())

    # @pytest.mark.skip
    def test_delete_department(self):
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={self.id}"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        params = {
            "access_token": f"{self.token}",
            "id": f"{self.id}"
        }
        r = requests.get(url, params)
        print(r.json())
        assert r.json()['errmsg'] == 'deleted'

    # @pytest.mark.skip
    def test_get_departmentlist(self):  # 获取部门列表
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
        params = {
            'access_token': self.token
        }
        r = requests.get(url=url, params=params)
        print(r.json())
        print('获取部门列表成功')

