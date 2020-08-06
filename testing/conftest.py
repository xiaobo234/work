#/usr/local/bin/python3.7
# -*- coding:utf-8 -*-
# import sys,os
# sys.path.append('./testing')
import requests
import pytest
@pytest.fixture()
def login():
    url='https://npro.test.100url.cn/adminapi/login'
    header={"content-type":"application/json;charset=UTF-8"}
    pay={"mobile":"15801409675","pwd":"123456","force": True}
    re=requests.post(url=url,headers=header,json=pay)
    print(re.status_code)
    #print(re.text)
    print(re.json()['data']['sessionId'])
    return re.json()['data']['sessionId'] #获取登录后返回数据中的token值
    #print(re.text)

# test_login()