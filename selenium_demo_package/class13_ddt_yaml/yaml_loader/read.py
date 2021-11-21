'''
    读取yaml中的文件内容
'''

import yaml

# 获取文件
# file = open('../data/data_dict.yaml', 'r', encoding='utf-8')
# file = open('../data/data_list.yaml', 'r', encoding='utf-8')
# file = open('../data/data.yaml', 'r', encoding='utf-8')
# file = open('../data/data1.yaml', 'r', encoding='utf-8')
# file = open('../data/data_type.yaml', 'r', encoding='utf-8')
# file = open('../data/data2.yaml', 'r', encoding='utf-8')
file = open('../data/data3.yaml', 'r', encoding='utf-8')

# 读取yaml文件内容
data = yaml.load(stream=file, Loader=yaml.FullLoader)
print(data)
# {'key': 'value', 'key1': 'value1', 'key2': 'value2'}
# ['value', 'value1', 'value2']
# [['a', 'b', 'c'], {'key': 'value', 'key1': 'value1'}, [{'key1.1': 'value1.1'}]]
# {'key1': {'key1.1': 'value1.1'}, 'key2': {'key2.1': {'key2.1.1': 'value2.1.1'}}, 'key3': ['a', 'b', 'c'], 'key4': [{'key4.1.1': [{'key4.1.1.1': 'value4.1.1.1'}]}]}
'''
{'user': 'xiaoming', 'age': 18, 
'defaults': {'user': 'shanjing', 'age': 18}, 
'shopinfo': {'user': 'shanjing', 'age': 18, 'url': 'shopxo.com'}, 
'baiduinfo': {'user': 'shanjing', 'age': 18, 'url': 'baidu.com'}}
'''
# ['XiaoMing', 'xiaohong', 'XiaoMing']
