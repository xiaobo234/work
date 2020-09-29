#/usr/local/bin/python3.7
# -*- coding:utf-8 -*-
import pytest
import requests
import allure

#内容管理测试用例
@allure.feature('内容管理')
class Testcase:
    @allure.title('进入内容管理模块主页') #测试报告中增加测试用例的标题
    @allure.severity('blocker')  #测试用例的级别
    @allure.story('进入内容管理模块主页') #测试用例的故事，相当于大功能模块的测试点用例
    def test_index(self,login):
        '''内容管理-进入内容管理模块主页'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/task/list?pageNo=1&pageSize=10&enterpriseId=&title=&businessId='
        with allure.step('请求数据'):
            res = requests.get(url=url, headers=header)
            print(res.status_code)
            print(res.json()) #将返回的json数据转换成字典，然后打印出来
        with allure.step('进行断言'):
            assert res.status_code==200  #从返回值种取出数据，然后用此数据进行断言

    @allure.title('按企业名称查询')
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
    @allure.title('代表发送按钮功能')
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
        assert res.json()['data']['data'][0]["userName"]=='代表A'  #从返回值种取出数据，然后用此数据进行断言
    @allure.title('代表未发送按钮功能')
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
        assert res.json()['data']['data'][1]["userName"]=='管理员'  #从返回值种取出数据，然后用此数据进行断言
    @allure.title('浏览客户按钮功能')
    @allure.story('浏览客户按钮')
    def test_read(self,login):
        '''内容管理-浏览客户按钮功能'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url='https://npro.test.100url.cn/adminapi/customer/customers?taskId=106&pageNo=1&pageSize=10&enterpriseId=&externalUserName=&externalUserMobile=&eventType=2'
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][0]["userName"]=='暖阳'  #从返回值种取出数据，然后用此数据进行断言
    @allure.title('打开客户按钮功能')
    @allure.story('打开客户按钮')
    def test_open(self,login):
        '''内容管理-打开客户按钮功能'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url='https://npro.test.100url.cn/adminapi/customer/customers?taskId=106&pageNo=1&pageSize=10&enterpriseId=&externalUserName=&externalUserMobile=&eventType=3'
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][0]["userName"]=='暖阳'  #从返回值种取出数据，然后用此数据进行断言

    @allure.title('收到客户按钮功能')
    @allure.story('收到客户按钮')
    def test_receive(self,login):
        '''内容管理-收到客户按钮功能'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url='https://npro.test.100url.cn/adminapi/customer/customers?taskId=106&pageNo=1&pageSize=10&enterpriseId=&externalUserName=&externalUserMobile=&eventType=1'
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][0]["userName"]=='暖阳'  #从返回值种取出数据，然后用此数据进行断言
    @allure.title('转发用户按钮功能')
    @allure.story('转发用户按钮')
    def test_transmit(self,login):
        '''内容管理-转发用户按钮功能'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url='https://npro.test.100url.cn/adminapi/customer/customers?taskId=106&pageNo=1&pageSize=10&enterpriseId=&externalUserName=&externalUserMobile=&eventType=5'
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][0]["userName"]=='暖阳'  #从返回值种取出数据，然后用此数据进行断言

    @allure.title('转化用户浏览按钮功能')
    @allure.story('转化用户浏览按钮')
    def test_transmitread(self,login):
        '''内容管理-转化用户浏览按钮'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url='https://npro.test.100url.cn/adminapi/customer/conversionusers?pageNo=1&pageSize=10&representativeName=&enterpriseId=&registerTimeStart=&registerTimeEnd=&taskId=106'
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][0]["externalUserName"]=='暖阳'  #从返回值种取出数据，然后用此数据进行断言
    @allure.title('翻页')
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
