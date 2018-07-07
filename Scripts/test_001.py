import yaml


#
# data = {'Search_Data': {
#                 'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
#                 'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}
#
# with open("./test_data.yaml", "a") as f:
#     yaml.dump(data, f, encoding="utf-8", allow_unicode=True)

"""
 data = {'Search_Data': 
            {
            'search_test_002': {'expect': '不好', 'value': '你好'}, 
            'search_test_001': {'expect': 15, 'value': 456}
        }}
"""

# 目标 [("你好","不好"),(456，15)]
# 思路： 1.取Search_Data值 ->2.取values -> 3.在取values???


param_list = []
with open("./test_data.yaml",'r') as f:
    # 读取文件
    data = yaml.load(f)

    for i in data.get("Search_Data").values():
        param_list.append((i.get("value"), i.get("expect")))

print(param_list)

# 参数值传递方式：
# pytest.mark.parametrize("输入参数, 输出预期结果",[(,)])
# 参数值：  多个参数 [(a,b)], 单个参数 ["a","b"]
