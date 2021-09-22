# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/9/22
Project ： PyCharm
File  : department
E-mail: zh13997821732@163.com


================================================================================

"""
import requests

from api_automation_course_test.apis.test_wework1 import WeWork
from jsonpath import jsonpath


class Department(WeWork):

    def create_department(self, data):
        """
        创建部门
        :param data:
        :return:
        """
        create_url = f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}'
        r = requests.post(url=create_url, json=data)
        return r.json()

    def update_department(self, data):
        """
        更新/修改部门信息
        :param data:
        :return:
        """
        updata_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        r = requests.post(url=updata_url, json=data)
        return r.json()

    def get_departmentlist(self):
        """
        获取部门列表
        :param data:
        :return:
        """
        get_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        r = requests.get(url=get_url)
        return r.json()

    def delete_department(self, depart_id):
        """
        删除单个部门
        :return:
        """
        del_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={depart_id}"
        r = requests.get(url=del_url)
        return r.json()

    def clear_department(self):
        """
        清理部门id非1和2的部门
        :return:
        """
        depart_list = self.get_departmentlist()
        id_list = jsonpath(depart_list, "$..id")
        for i in id_list:
            if i != 1 and i != 2:
                self.delete_department(i)

        return id_list


if __name__ == '__main__':
    a = Department()
    print(a.clear_department())
