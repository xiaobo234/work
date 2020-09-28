# -*- coding:utf-8 -*-
import pytest
import requests
import allure
#客户管理测试用例
@allure.feature('模板管理')
class Testcase:
    @allure.title('获取全部功能')
    @allure.story('获取全部功能列表')
    def test_index(self,login):
        '''模板管理-获取全部功能列表'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url='https://npro.test.100url.cn/adminapi/template/func'
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.json()['data']['data'][0]['typeName']=='线下拜访'  #从返回值种取出数据，然后用此数据进行断言

    @allure.title('获取租户开通的功能列表')
    @allure.story('查看开通的功能列表')
    def test_zuhukaitong(self,login):
        '''模板管理-开通功能列表'''
        with allure.step('第一步：准确请求数据'):
            header = {
                "content-type": "application/json",
                "sessionId": login,
            }
            url = 'https://npro.test.100url.cn/adminapi/template/func/19'
        with allure.step('第二步：请求'):
            res = requests.get(url=url, headers=header)
            print(res.json()) #将返回的json数据转换成字典，然后打印出来
        with allure.step('第三步：断言'):
            assert res.json()['data']['data'][0]['enterpriseId']==19  #从返回值种取出数据，然后用此数据进行断言

    @allure.title('获取模板列表')
    @allure.story('获取模板的列表')
    def test_temple(self,login):
        '''模板管理-开通功能列表'''
        with allure.step('第一步：准确请求数据'):
            header = {
                "content-type": "application/json",
                "sessionId": login,
            }
            url = 'https://npro.test.100url.cn/adminapi/template/get/19'
        with allure.step('第二步：请求'):
            res = requests.get(url=url, headers=header)
            print(res.json()) #将返回的json数据转换成字典，然后打印出来
        with allure.step('第三步：断言'):
            assert res.json()['data']['data'][0]['enterpriseId']==19  #从返回值种取出数据，然后用此数据进行断言
    @allure.title('模板控件')
    @allure.story('获取模板控件列表')
    def test_control(self,login):
        '''模板管理-获取模板控件列表'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url='https://npro.test.100url.cn/adminapi/template/4/controls'
        res = requests.get(url=url, headers=header)
        assert res.status_code == 200  #从返回值种取出数据，然后用此数据进行断言

    @allure.title('控件类型')
    @allure.story('获取控件类型列表')
    def test_controltypes(self,login):
        '''模板管理-获取控件类型列表'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url='https://npro.test.100url.cn/adminapi/template/controlTypes'
        res = requests.get(url=url, headers=header)
        assert res.json()['data']['data'][0]['typeName']=='TEXT_SINGLE'  #从返回值种取出数据，然后用此数据进行断

    @allure.story('翻页')
    def test_fanye(self, login):
        '''客户管理-翻页'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url = 'https://npro.test.100url.cn/adminapi/visit/list?pageSize=10&pageNo=2&enterpriseId=&userName=&startTime=&endTime='
        res = requests.get(url=url, headers=header)
        print(res.json())  # 将返回的json数据转换成字典，然后打印出来
        assert res.status_code == 200  # 从返回值种取出数据，然后用此数据进行断言