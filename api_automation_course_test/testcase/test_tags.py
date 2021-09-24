# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/9/23
Project ： PyCharm
File  : test_tags
E-mail: zh13997821732@163.com


================================================================================

"""
from time import sleep

import allure

from api_automation_course_test.apis.tags import Tags
from api_automation_course_test.testcase.utils import Utils


@allure.feature("标签模块")
class TestTags:
    def setup_class(self):
        conf_data = Utils.get_datas('../data/api.yaml')
        corpid = conf_data['corpid']
        corpsecret = conf_data['corpsecret']
        print('类初始化')
        # 实例化标签类
        self.tags = Tags(corpid, corpsecret)
        # 清理标签
        self.tags.clear_tags()
        # 实例化工具类，生成随机的tagid
        self.data = Utils()
        self.tagid = self.data.get_random_number()
        self.tagname = self.data.get_random_tagname()
        # 创建标签数据
        self.create_tag_data = {
            "tagname": self.tagname,
            "tagid": self.tagid
        }
        # 更新标签数据
        self.update_tag_data = {
            "tagid": self.tagid,
            "tagname": f"{self.tagname}-update"
        }
        self.add_tagmember_data = {
            "tagid": self.tagid,
            "userlist": ['446532056']
        }
        self.del_tagmember_data = {
            "tagid": self.tagid,
            "userlist": ['446532056']
        }

    @allure.story("标签场景用例")
    def test_tags_scene(self):
        # 创建标签
        with allure.step("创建单个标签"):
            self.tags.create_tag(self.create_tag_data)
        # 标签中添加成员
        with allure.step("在新增标签中添加成员"):
            self.tags.add_tag_member(self.add_tagmember_data)
            userlist = Utils.base_jsonpath(self.tags.get_tag_member(self.tagid), "$..userid")
            assert '446532056' in userlist
            print("给成员添加标签成功")
            print(self.tags.get_tag_member(self.tagid))
        #删除标签中的成员
        with allure.step("删除标签中的成员"):
            self.tags.delete_tag_member(self.del_tagmember_data)
        with allure.step("获取删除后的标签中的成员"):
            print(self.tags.get_tag_member(self.tagid))

            id_list = Utils.base_jsonpath(self.tags.get_tag_member(self.tagid), "$.userlist")
            print(id_list)
            assert "446532056" not in id_list
            print("删除指定标签中的成员成功")
        # 获取标签列表
        with allure.step("获取标签列表"):
            tags_list = Utils.base_jsonpath(self.tags.get_tagslist(), "$..tagid")
            print(self.tags.get_tagslist())
            assert self.tagid in tags_list
            print("创建标签成功")
        with allure.step("更新单个标签"):
            self.tags.update_tag(self.update_tag_data)
            tagsname_list = Utils.base_jsonpath(self.tags.get_tagslist(), "$..tagname")
            print(self.tags.get_tagslist())
            assert f"{self.tagname}-update" in tagsname_list
            print("修改标签成功")
        # 删除标签
        with allure.step("删除标签"):
            self.tags.delete_tag(self.tagid)
        # 获取标签列表断言删除后的tagid是否不存在
        with allure.step("获取删除后的部门列表"):
            del_tagslist = Utils.base_jsonpath(self.tags.get_tagslist(), "$..tagid")
            print(del_tagslist)
            assert self.tagid not in del_tagslist
            print("删除标签成功")
