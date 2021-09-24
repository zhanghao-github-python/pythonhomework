# -*- coding: utf-8 -*-
"""
================================================================================

Author : Administrator
Created  on : 2021/9/23
Project ： PyCharm
File  : tags
E-mail: zh13997821732@163.com


================================================================================

"""
from api_automation_course_test.apis.test_wework import WeWork
from api_automation_course_test.testcase.utils import Utils


class Tags(WeWork):
    def create_tag(self, data):
        """
        创建标签
        :param data:
        :return:
        """
        create_url = f'https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}'
        req = {
            "method": "POST",
            "url": create_url,
            "json": data
        }
        r = self.send_api(req)
        return r.json()

    def update_tag(self, data):
        """
        更新标签
        :param data:
        :return:
        """
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        req = {
            "method": "POST",
            "url": update_url,
            "json": data
        }
        r = self.send_api(req)
        return r.json()

    def get_tagslist(self):
        """
        获取全部标签列表
        :return:
        """
        get_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        req = {
            "method": "GET",
            "url": get_url
        }
        r = self.send_api(req)
        return r.json()

    def delete_tag(self, tag_id):
        """
        删除单个标签
        :param tag_id:
        :return:
        """
        del_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tag_id}"
        req = {
            "method": "GET",
            "url": del_url
        }
        r = self.send_api(req)
        return r.json()

    def clear_tags(self):
        tags_list = self.get_tagslist()
        tags_ids = Utils.base_jsonpath(tags_list, "$..tagid")
        for i in tags_ids:
            if i != 1:
                self.delete_tag(i)
        return tags_ids

    def get_tag_member(self, tagid):
        """
        获取指定单个标签内的成员
        :return:
        """
        member_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tagid}"
        req = {
            "method": "GET",
            "url": member_url
        }
        r = self.send_api(req)
        return r.json()

    def add_tag_member(self, data):
        """
        在标签中添加成员
        :param data:
        :return:
        """
        add_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token={self.token}"
        req = {
            "method": "POST",
            "url": add_member_url,
            "json": data
        }
        r = self.send_api(req)
        return r.json()

    def delete_tag_member(self, data):
        """
        删除标签中的成员
        :return:
        """
        del_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers?access_token={self.token}"
        req = {
            "method": "POST",
            "url": del_url,
            "json": data
        }
        r = self.send_api(req)
        return r.json()


if __name__ == '__main__':
    conf_data = Utils.get_datas('../data/api.yaml')
    corpid = conf_data['corpid']
    corpsecret = conf_data['corpsecret']
    tags = Tags(corpid, corpsecret)
    # print(tags.get_tagslist())
    print(tags.get_tag_member(1))