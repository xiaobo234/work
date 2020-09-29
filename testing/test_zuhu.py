#/usr/local/bin/python3.7
# -*- coding:utf-8 -*-
import pytest
import requests
import allure
from  jsonpath  import jsonpath
from hamcrest import *  #hamcrest第三方的库，一种断言方式

#租户管理测试用例
@allure.feature('租户管理')
class Testcase:
    @allure.title('进入租户管理模块主页')
    @allure.story('获取企业微信一级部门列表')
    def test_dept(self,login):
        '''租户管理-进入租户管理模块主页'''
        with allure.step('第一步：准确请求数据'):
            header = {
                "content-type": "application/json",
                "sessionId": login,
            }
            url = 'https://npro.test.100url.cn/adminapi/dept/depts?deptName=&pageNo=1&pageSize=10'
        with allure.step('第二步：请求'):
            res = requests.get(url=url, headers=header)
            print(res.status_code)
            print(res.json()) #将返回的json数据转换成字典，然后打印出来
        with allure.step('第三步：断言'):
            assert res.json()['data']['data'][0]["wechatDeptName"]=='医百测试平台'  #从返回值种取出数据，然后用此数据进行断言
    @allure.story('获取租户下拉绑定列表')
    def test_enterprises(self, login):
        '''租户管理-租户下拉绑定列表'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url='https://npro.test.100url.cn/adminapi/dept/enterprises'
        res = requests.get(url=url, headers=header)
        print(res.json())  # 将返回的json数据转换成字典，然后打印出来
        assert res.status_code == 200  # 从返回值种取出数据，然后用此数据进行断言

    @allure.story('停用租户')
    def test_disable(self, login):
        '''租户管理-租户下拉绑定列表'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url='https://npro.test.100url.cn/adminapi/dept/disable'
        data={"id":12}
        res = requests.post(url=url, json=data,headers=header)
        print(res.json())  # 将返回的json数据转换成字典，然后打印出来
        assert res.status_code == 200  # 从返回值种取出数据，然后用此数据进行断言

    @allure.story('启用租户')
    def test_enable(self, login):
        '''租户管理-启用租户'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url='https://npro.test.100url.cn/adminapi/dept/enable'
        data={"id":12}
        res = requests.post(url=url, json=data,headers=header)
        print(res.json())  # 将返回的json数据转换成字典，然后打印出来
        assert res.status_code == 200  # 从返回值种取出数据，然后用此数据进行断言

    @allure.story('添加企业微信部门与saas租户的mapping关系')
    def test_mapping(self, login):
        '''租户管理-与saas租户mapping关系'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url='https://npro.test.100url.cn/adminapi/dept/mapping'
        data={"id":5,"saasCompanyUrl":"kk.100live.cn"}
        res = requests.post(url=url, json=data,headers=header)
        assert res.json()['code']==0 # 从返回值种取出数据，然后用此数据进行断言

    @allure.title('按企业名称查询')
    @allure.story('按企业名称查询')
    def test_zuhufind(self,login):
        '''线下拜访-按企业名称查询'''
        with allure.step('第一步：准确请求数据'):
            header = {
                "content-type": "application/json",
                "sessionId": login,
            }
            url = 'https://npro.test.100url.cn/adminapi/visit/list?pageSize=10&pageNo=1&enterpriseId=19&userName=&startTime=&endTime='
        with allure.step('第二步：请求'):
            res = requests.get(url=url, headers=header)
            print(res.status_code)
            print(res.json()) #将返回的json数据转换成字典，然后打印出来
        with allure.step('第三步：断言'):
            assert res.json()['data']['data'][0]["deptName"]=='医百测试平台'  #从返回值种取出数据，然后用此数据进行断言

    @allure.story('翻页')
    def test_fanye(self, login):
        '''客户管理-翻页'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/customer/customers?pageNo=2&pageSize=10&enterpriseId=&externalUserName=&externalUserMobile='
        res = requests.get(url=url, headers=header)
        print(res.json())  # 将返回的json数据转换成字典，然后打印出来
        assert res.status_code == 200  # 从返回值种取出数据，然后用此数据进行断言