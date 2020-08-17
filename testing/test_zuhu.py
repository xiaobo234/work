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
    @allure.story('进入租户管理模块主页')
    def test_index(self,login):
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
            assert res.json()['data']['data'][0]["wechatDeptName"]=='沙海科技有限公司'  #从返回值种取出数据，然后用此数据进行断言
    @allure.title('按企业名称查询')
    @allure.story('按企业名称查询')
    def test_zuhufind(self,login):
        '''租户管理-按企业名称查询'''
        with allure.step('第一步：准确请求数据'):
            header = {
                "content-type": "application/json",
                "sessionId": login,
            }
            url = 'https://npro.test.100url.cn/adminapi/dept/depts?deptName=医百测试平台&pageNo=1&pageSize=10'
        with allure.step('第二步：请求'):
            res = requests.get(url=url, headers=header)
            print(res.status_code)
            print(res.json()) #将返回的json数据转换成字典，然后打印出来
        with allure.step('第三步：断言'):
            assert res.json()['data']['data'][0]["wechatDeptName"]=='医百测试平台'  #从返回值种取出数据，然后用此数据进行断言
    @allure.title('进入用户管理主页')
    @allure.story('进入用户管理主页')
    def test_userindex(self,login):
        '''租户管理-进入用户管理主页'''
        with allure.step('第一步：准确请求数据'):
            header = {
                "content-type": "application/json",
                "sessionId": login,
            }
            url = 'https://npro.test.100url.cn/adminapi/user/users?pageNo=1&pageSize=10&enterpriseId=19&mobile='
        with allure.step('第二步：请求'):
            res = requests.get(url=url, headers=header)
            print(res.json()) #将返回的json数据转换成字典，然后打印出来
        with allure.step('第三步：断言'):
            assert res.json()['data']['data'][0]["mobile"]=='17310141813'  #从返回值种取出数据，然后用此数据进行断言
            assert_that(res.json()['data']['data'][0]["mobile"],'17310141813') #用asser_that方式进行断言
            assert jsonpath(res.json(),'$..mobile')[0]=="17310141813" #用jsonpath的方式匹配响应数据中的值，然后进行断言，
    @allure.title('用户管理主页-查询功能')
    @allure.story('用户管理主页-查询')
    def test_userfind(self,login):
        '''租户管理-用户管理主页-查询'''
        with allure.step('第一步：准确请求数据'):
            header = {
                "content-type": "application/json",
                "sessionId": login,
            }
            url = 'https://npro.test.100url.cn/adminapi/user/users?pageNo=1&pageSize=10&enterpriseId=19&mobile=17310141813'
        with allure.step('第二步：请求'):
            res = requests.get(url=url, headers=header)
            print(res.json()) #将返回的json数据转换成字典，然后打印出来
        with allure.step('第三步：断言'):
            assert res.json()['data']['data'][0]["mobile"]=='17310141813'  #从返回值种取出数据，然后用此数据进行断言

    @allure.story('翻页')
    def test_fanye(self, login):
        '''客户管理-翻页'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/dept/depts?deptName=&pageNo=2&pageSize=10'
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json())  # 将返回的json数据转换成字典，然后打印出来
        assert res.status_code == 200  # 从返回值种取出数据，然后用此数据进行断言