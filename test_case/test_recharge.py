from tools.api import request_tool
import requests
import random
import allure

from config.conf import API_URL

@allure.feature("用户管理")
@allure.story("充值提现模块")
@allure.title("扣款接口")
def test_recharge(db):
    # 执行查询语句
    with allure.step("第一步，查询数据库"):
        res=db.select_execute("select account_name from t_cst_account where status=0 and account_name is not null")
    with allure.step("第二步，从随机获取的数据中选第一个数据"):
        account_name=random.choice(res)[0]
    data={
        "accountName":account_name,
        "changeMoney":1000
    }
    r=requests.request("POST",API_URL+"/acc/charge",json=data)
    with allure.step("第三步获取请求"):
        allure.attach(r.request.method,"请求方法",allure.attachment_type.TEXT)
        allure.attach(r.request.url,"请求url",allure.attachment_type.TEXT)
        allure.attach(str(r.request.headers),"请求头",allure.attachment_type.TEXT)
        allure.attach(r.request.body,"请求正文",allure.attachment_type.TEXT)
# pytest test_case/test_recharge.py --alluredir=reports/yahooxml

# allure generate reports/yahooxml -o reports/giaohtml