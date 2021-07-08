# -*- coding:utf-8 -*-
import pytest
import requests
import allure
#客户管理测试用例
@allure.feature('用户管理')
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