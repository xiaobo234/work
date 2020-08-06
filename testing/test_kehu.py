#/usr/local/bin/python3.7
# -*- coding:utf-8 -*-
import pytest
import requests

#客户管理测试用例
class Testcase:
    def test_index(self,login):
        '''客户管理-进入代表管理模块主页'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/customer/customers?pageNo=1&pageSize=10&enterpriseId=&externalUserName=&externalUserMobile='
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][0]["deptName"]=='沙海科技有限公司'  #从返回值种取出数据，然后用此数据进行断言
    def test_indexfind(self,login):
        '''客户管理-按企业名称+手机号查询'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/customer/customers?pageNo=1&pageSize=10&enterpriseId=19&externalUserName=&externalUserMobile=15383153086'
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][0]["deptName"]=='医百测试平台'  #从返回值种取出数据，然后用此数据进行
    def test_fanye(self, login):
        '''客户管理-翻页'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url='https://npro.test.100url.cn/adminapi/customer/customers?pageNo=2&pageSize=10&enterpriseId=&externalUserName=&externalUserMobile='
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json())  # 将返回的json数据转换成字典，然后打印出来
        assert  res.status_code==200  # 从返回值种取出数据，然后用此数据进行断言
