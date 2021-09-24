# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/9/22
Project ： PyCharm
File  : test_department
E-mail: zh13997821732@163.com


================================================================================

"""
import allure

from api_automation_course_test.apis.department import Department
from api_automation_course_test.testcase.utils import Utils
from app_automation_course_test.utils.get_datas import GetData


@allure.feature("部门管理模块")
class TestDepartment:
    def setup_class(self):
        # 实例化部门类
        conf_data = Utils.get_datas('../data/api.yaml')
        corpid = conf_data['corpid']
        corpsecret = conf_data['corpsecret']
        print('类初始化')
        self.department = Department(corpid, corpsecret)
        # 清理部门
        self.department.clear_department()
        # 预置测试数据
        a = GetData()  # 获取随机部门名称和随机id
        self.departmentname = a.get_department_name()
        self.id = a.get_random_number()
        self.create_data = {
            "name": f"{self.departmentname}",
            "parentid": 1,
            "id": f"{self.id}"
        }
        self.update_data = {
            "id": f"{self.id}",
            "name": f"{self.departmentname}-update",
        }
    @allure.story("部门场景接口用例")
    def test_department_scene(self):
        """
        pytest --alluredir=./result/result 生成结果的命令在当前目录下生成result目录
        allure generate --clean result -o ./result/result/html  生成html
        --clean result报告覆盖之前的结果
        :return:
        """
        # 创建部门
        with allure.step("创建部门"):
            self.department.create_department(self.create_data)
        # 获取部门列表
        with allure.step("获取创建后的部门列表"):
            department_list = Utils.base_jsonpath(self.department.get_departmentlist(), "$..name")
            assert self.departmentname in department_list
        print(department_list)
        print("添加部门成功")
        # 更新部门
        with allure.step("更新部门"):
            self.department.update_department(self.update_data)
        # 获取所有的部门列表
        with allure.step("查询更新部门的结果"):
            updatedepartment_list = Utils.base_jsonpath(self.department.get_departmentlist(), "$..name")
            # 根据修改的部门名称做断言
            print(updatedepartment_list)
            assert f'{self.departmentname}-update' in updatedepartment_list
            print("更新部门成功")
        # 删除部门
        with allure.step("删除部门"):
            self.department.delete_department(f"{self.id}")
        # 获取删除后的部门列表
        with allure.step("获取删除后的部门列表"):
            del_id_list = Utils.base_jsonpath(self.department.get_departmentlist(), "$..id")
            print(del_id_list)
        with allure.step("删除部门的断言"):
            assert f"{self.id}" not in del_id_list
            print("删除部门成功")

    @allure.story("测试接口用例")
    def test_001(self):
         print('001')
