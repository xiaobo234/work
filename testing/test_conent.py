#/usr/local/bin/python3.7
# -*- coding:utf-8 -*-
import pytest
import requests
import allure

#内容管理测试用例
@allure.feature('内容管理')
class Testcase:
    @allure.story('进入内容管理模块主页')
    def test_index(self,login):
        '''内容管理-进入内容管理模块主页'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/task/list?pageNo=1&pageSize=10&enterpriseId=&title=&businessId='
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][0]["enterpriseName"]=='沙海科技有限公司'  #从返回值种取出数据，然后用此数据进行断言
    @allure.story('按企业名称查询')
    def test_indexfind(self,login):
        '''内容管理-按企业名称查询'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/task/list?pageNo=1&pageSize=10&enterpriseId=19&title=&businessId='
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][0]["enterpriseName"]=='医百测试平台'  #从返回值种取出数据，然后用此数据进行断言
    @allure.story('代表发送按钮功能')
    def test_fasong(self,login):
        '''内容管理-发送代表'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/representative/list?flag=1&taskId=47&pageNo=1&pageSize=10&userName=&mobile=&enterpriseId='
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][0]["userName"]=='管理员'  #从返回值种取出数据，然后用此数据进行断言
    @allure.story('未发送代表按钮')
    def test_nofasong(self,login):
        '''内容管理-未发送代表'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/representative/list?flag=2&taskId=54&pageNo=1&pageSize=10&userName=&mobile=&enterpriseId='
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][1]["userName"]=='代表B'  #从返回值种取出数据，然后用此数据进行断言
    @allure.story('阅读客户按钮')
    def test_read(self,login):
        '''内容管理-阅读客户'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/customer/customers?taskId=49&pageNo=1&pageSize=10&enterpriseId=&externalUserName=&externalUserMobile='
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][1]["representativeName"]=='代表A'  #从返回值种取出数据，然后用此数据进行断言
    @allure.story('翻页功能')
    def test_fanye(self, login):
        '''转化用户管理-翻页'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url='https://npro.test.100url.cn/adminapi/task/list?pageNo=2&pageSize=10&enterpriseId=&title=&businessId='
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json())  # 将返回的json数据转换成字典，然后打印出来
        assert  res.status_code==200  # 从返回值种取出数据，然后用此数据进行断言
