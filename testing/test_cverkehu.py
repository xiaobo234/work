#/usr/local/bin/python3.7
# -*- coding:utf-8 -*-
import pytest
import requests
import allure
#转化用户管理测试用例
@allure.feature('转化客户')
class Testcase:
    @allure.story('进入转化用户管理模块主页')
    def test_index(self,login):
        '''转化用户管理-进入转化用户管理模块主页'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/customer/conversionusers?pageNo=1&pageSize=10&representativeName=&registerTimeStart=&enterpriseId=&registerTimeEnd='
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][4]["nickName"]=='稳了兄弟'  #从返回值种取出数据，然后用此数据进行断言
    @allure.story('按企业名称查询')
    def test_indexfind(self,login):
        '''转化用户管理-按企业名称查询'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/customer/conversionusers?pageNo=1&pageSize=10&representativeName=&registerTimeStart=&enterpriseId=19&registerTimeEnd='
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][2]["nickName"]=='想你丶原来可以'  #从返回值种取出数据，然后用此数据进行断言
    @allure.story('翻页')
    def test_fanye(self, login):
        '''转化用户管理-翻页'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url='https://npro.test.100url.cn/adminapi/customer/conversionusers?pageNo=2&pageSize=10&representativeName=&registerTimeStart=&enterpriseId=&registerTimeEnd='
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json())  # 将返回的json数据转换成字典，然后打印出来
        assert  res.status_code==200  # 从返回值种取出数据，然后用此数据进行断言
