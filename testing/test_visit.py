# -*- coding:utf-8 -*-
import pytest
import requests
import allure
#客户管理测试用例
@allure.feature('线下拜访')
class Testcase:
    @allure.story('获取拜访列表')
    def test_index(self,login):
        '''线下拜访-进入线下拜访模块主页'''
        header = {
            "content-type": "application/json",
            "sessionId": login,
        }
        url='https://npro.test.100url.cn/adminapi/visit/list?pageSize=10&pageNo=1&enterpriseId=&userName=&startTime=&endTime='
        res = requests.get(url=url, headers=header)
        print(res.status_code)
        print(res.json()) #将返回的json数据转换成字典，然后打印出来
        assert res.status_code==200  #从返回值种取出数据，然后用此数据进行断言

    @allure.title('拜访详情')
    @allure.story('查看拜访详情')
    def test_userindex(self,login):
        '''租户管理-进入用户管理主页'''
        with allure.step('第一步：准确请求数据'):
            header = {
                "content-type": "application/json",
                "sessionId": login,
            }
            url = 'https://npro.test.100url.cn/adminapi/visit/77?id=77'
        with allure.step('第二步：请求'):
            res = requests.get(url=url, headers=header)
            print(res.json()) #将返回的json数据转换成字典，然后打印出来
        with allure.step('第三步：断言'):
            assert res.status_code==200  #从返回值种取出数据，然后用此数据进行断言

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