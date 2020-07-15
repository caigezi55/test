import pytest

from tools.api import request_tool

@pytest.mark.reaname
@pytest.mark.pick
def test_registers(pub_data):
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

@pytest.mark.reaname
@pytest.mark.pick
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

@pytest.mark.reaname
@pytest.mark.pick
# 跳过 @pytest.skip(5>2,reason='跳过')
def test_relname(pub_data):
    pub_data['certno']="自动生成 身份证号"
    pub_data['cstName']="自动生成 姓名"
    pub_data['email']="自动生成 邮箱"
    headers={"token":pub_data["token"]}
    method = "POST"  # 请求方法，全部大写
    feature = "用户实名认证"  # allure报告中一级分类
    story = 'realname'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/cst/realname2"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
            {
              "cstId": "${cstId}",
              "customerInfo": {
                "birthday": "2020-05-07", 
                "certno": "${certno}",
                "city": "上海",
                "cstName": "${cstName}",
                "email": "${email}",
                "province": "上海",
                "sex": 1
              }
            }
            '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, json_data=json_data, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title,headers=headers)
