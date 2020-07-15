#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tools.api import request_tool


def test_signUp(pub_data):
    pub_data["username"] = "自动生成 字符串 5,6 数字 xh"
    pub_data["phone"] = "自动生成 手机号"
    pub_data["pwd"]="a123456"
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/signup"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
                {
                  "phone": "${phone}",
                  "pwd": "${pwd}",
                  "rePwd": "${pwd}",
                  "userName": "${username}"
                }
                '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, json_data=json_data, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title)
    pub_data["cstId"]=r.json()["data"]["cstId"]

def test_login(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
                {
                  "pwd": "${pwd}",
                  "userName": "${username}"
                }
                '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, json_data=json_data, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title)
    pub_data["token"]=r.json()["data"]["token"]

def test_mekeMoney(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
                {
                  "accountName": "${username}",
                  "changeMoney": 50000
                }
              '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, json_data=json_data, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title)


def test_searchMoney(pub_data):
    method = "GET"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询余额'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getAccInfo"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params={"accountName":"${username}"}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, params=params, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title)


def test_withdraw(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '提现'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/withdraw"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data='''
            {
                "accountName": "${username}",
                "cardNo": "4561234586254",
                "changeMoney": 500
            }
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, json_data=json_data, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title)

def test_searchMoney2(pub_data):
    method = "GET"  # 请求方法，全部大写
    feature = "用户模块2"  # allure报告中一级分类
    story = '查询余额'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getAccInfo"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params={"accountName":"${username}"}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, params=params, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title)


def test_accLock(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '账户冻结'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/accLock"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data={"accountName":"${username}"}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, data=data, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title)

def test_accUnLock(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '账户解冻'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/accUnLock"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data={"accountName":"${username}"}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, data=data, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title)



def test_mekeMoney2(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
                {
                  "accountName": "${username}",
                  "changeMoney": 50000
                }
              '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, json_data=json_data, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title)


def test_withdraw2(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '提现'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/withdraw"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data='''
            {
                "accountName": "${username}",
                "cardNo": "4561234586254",
                "changeMoney": 500
            }
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, json_data=json_data, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title)

def test_searchMoney2(pub_data):
    method = "GET"  # 请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询余额'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getAccInfo"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params={"accountName":"${username}"}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, params=params, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title)

