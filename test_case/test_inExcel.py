import pytest
import os
from tools.data import excel_tool
from tools.api import request_tool

data=excel_tool.get_test_case("D:\\pyCharm folder\\7_13file\\test_case\\金额充值测试.xlsx")
@pytest.mark.parametrize("accountName,changeMoney,expect",data[1],ids=data[0])
def test_inExcel(pub_data,accountName,changeMoney,expect):
    pub_data["account_name"]=accountName
    pub_data["money"]=changeMoney
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = expect  # 预期结果
    json_data='''{
      "accountName": "luomh82",
      "changeMoney": 111
    }'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)