#/usr/local/bin/python3.7
# -*- coding:utf-8 -*-

import pytest
import requests
#空中课堂测试用例
class Testcase:
    def test_zuhufind(self,login):
        '''租户管理-按企业名称查询'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/dept/depts?deptName=医百测试平台&pageNo=1&pageSize=10'
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][0]["wechatDeptName"]=='医百测试平台'  #从返回值种取出数据，然后用此数据进行断言
    def test_userindex(self,login):
        '''租户管理-进入用户管理主页'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/user/users?pageNo=1&pageSize=10&enterpriseId=19&mobile='
        res = requests.get(url=url, headers=header)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][0]["mobile"]=='17310141813'  #从返回值种取出数据，然后用此数据进行断言
    def test_userfind(self,login):
        '''租户管理-用户管理主页-查询'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/user/users?pageNo=1&pageSize=10&enterpriseId=19&mobile=17310141813'
        res = requests.get(url=url, headers=header)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][0]["mobile"]=='17310141813'  #从返回值种取出数据，然后用此数据进行断言