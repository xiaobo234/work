#/usr/local/bin/python3.7
# -*- coding:utf-8 -*-
import pytest
import requests
#代表管理测试用例

class Testcase:
    def test_index(self,login):
        '''代表管理-进入代表管理模块主页'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/representative/list?pageNo=1&pageSize=10&userName=&mobile=&enterpriseId='
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][0]["deptName"]=='沙海科技有限公司'  #从返回值种取出数据，然后用此数据进行断言
    def test_indexfind(self,login):
        '''代表管理-按企业名称+手机号查询'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/representative/list?flag=&taskId=&pageNo=1&pageSize=10&userName=&mobile=15801409675&enterpriseId=19'
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][0]["mobile"]=='15801409675'  #从返回值种取出数据，然后用此数据进行断言
    def test_kehufind(self,login):
        '''代表管理-客户管理按钮'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/customer/customers?representativeUid=30&pageNo=1&pageSize=10&enterpriseId=&externalUserName=&externalUserMobile='
        res = requests.get(url=url, headers=header)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][0]["deptName"]=='医百测试平台'  #从返回值种取出数据，然后用此数据进行断言
    def test_datail(self,login):
        '''代表管理-查看详情'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/static/js/chunk-35b89256.c0909af9.js'
        res = requests.get(url=url, headers=header)
        # print(res.json()) #将返回的json数据转换成字典，然后打印出来
        # assert res.status_code==200  #从返回值种取出数据，然后用此数据进行断言