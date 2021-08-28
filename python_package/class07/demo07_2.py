'''
正则表达式：
用来处理字符串
特点：灵活
导入正则：import re
匹配规则：
    \d 匹配数字
    \D 匹配非数字
    \w 匹配字母、数字、下划线、中文
    \W 匹配非字母、数字、下划线、中文
    . 匹配任意字符，除\n以外
    {} 前面元素出现的次数 例如：\d{3} 匹配三个数字
    ？非贪婪模式 匹配0个或1个表达式
    + 匹配1个或多个表达式
    * 匹配0个或多个表达式

常用方法:
    match()：只匹配开头。 尝试从字符串的起始位置匹配，如果起始位置没有匹配成功的话，match()就返回none。
    search()：扫描整个字符串并返回第一个成功的匹配。匹配成功re.search方法返回一个匹配的对象，否则返回None。
    findall()：扫描整个字符串并返回所有成功的匹配。

re.match与re.search的区别
    re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，而 re.search 匹配整个字符串，直到找到一个匹配。

group(num) 或 groups()

'''
# 导入正则
import re


# # match():只匹配开头。 尝试从字符串的起始位置匹配，如果起始位置没有匹配成功的话，match()就返回none。
# str1 = '1234567890qwert-=~!@#$%^&*()_+[]df1234567890sdf\{}|;:,./<>?asda'
# # 匹配数字
# res = re.match('\d', str1)
# print(res)  # <re.Match object; span=(0, 1), match='1'>
# res = re.match('\d{3}', str1)
# print(res)  # <re.Match object; span=(0, 3), match='123'>
# res = re.match('\d+', str1)
# print(res)  # <re.Match object; span=(0, 10), match='1234567890'>
# str2 = 'qwert-=~!@#$%^&*()_+[]df1234567890sdf\{}|;:,./<>?asda'
# res = re.match('\d+', str2)
# print(res)  # None

# search(): 扫描整个字符串并返回第一个成功的匹配。匹配成功re.search方法返回一个匹配的对象，否则返回None。
# str1 = '1234567890qwert-=~!@#$%^&*()_+[]df1234567890sdf\{}|;:,./<>?asda'
# # 匹配数字
# res = re.search('\d', str1)
# print(res)  # <re.Match object; span=(0, 1), match='1'>
# str2 = 'qwert-=~!@#$%^&*()_+[]df1234567890sdf\{}|;:,./<>?asda'
# res = re.search('\d+', str2)
# print(res)  # <re.Match object; span=(24, 34), match='1234567890'>

# 我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
# str1 = '1234567890qwert-=~!@#$%^&*()_+[]df1234567890sdf\{}|;:,./<>?asda'
# res = re.match('\d+', str1)
# print(res)  # <re.Match object; span=(0, 10), match='1234567890'>
# res = re.match('\d+', str1).group() # 1234567890
# print(res)  # <re.Match object; span=(0, 10), match='1234567890'>
#
# res = re.search('\d+', str1)  # 1234567890
# print(res)  # <re.Match object; span=(0, 10), match='1234567890'>
# res = re.search('\d+', str1).group()  # 1234567890
# print(res)  # 1234567890

# findall()：扫描整个字符串并返回所有成功的匹配。
# str1 = '1234567890qwert-=~!@#$%^&*()_+[]df1234567890sdf\{}|;:,./<>?asda'
# # 匹配数字
# res = re.findall('\d', str1)
# print(res)  # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# str2 = 'qwert-=~!@#$%^&*()_+[]df1234567890sdf\{}|;:,./<>?asda'
# res = re.findall('\d+', str2)
# print(res)  # ['1234567890']


# 匹配数字和字母，但不匹配问号
# str1 = '1234567890qwert-=~!@#$%^&*()_+[]df1234567890sdf\{}|;:,./<>?asda'
# res = re.findall('\w+',str1)
# print(res)  # ['1234567890qwert', '_', 'df1234567890sdf', 'asda']

# 12、字符串"Hey, you - what are you doing here!?"
# 分割成
# 'Hey', 'you', 'what', 'are', 'you', 'doing', 'here'
# str1 = "Hey, you - what are you doing here!?"
# res = re.findall('\w+', str1)
# print(res)  # ['Hey', 'you', 'what', 'are', 'you', 'doing', 'here']
# res = re.findall(r'[\w]+', str1)
# print(res)  # ['Hey', 'you', 'what', 'are', 'you', 'doing', 'here']

# 贪婪模式与非贪婪模式
# # 贪婪模式 *
# rel = re.search('e.*a', 'abcde123a123a')
# print(rel)  # <re.Match object; span=(4, 13), match='e123a123a'>
# # 非贪婪模式 ?
# rel = re.search('e.*?a', 'abcde123a123a')
# print(rel)  # <re.Match object; span=(4, 9), match='e123a'>
#
# img2 = "<img src='test.jpg' width='20px' height='28px'>"
# rel = re.search('src=.*? ', img2).group()
# print(rel)  # src='test.jpg'


# 递归：函数内部自己调用自己  顾名思义：有去有回
# 递归需要有一个出口（即终止条件），否则会陷入死循环
# def sum_num(num):
#     print(num)
#       终止条件
#     if (num == 1):
#         return 1
#     sum_num(num - 1)
#
#
# sum_num(10)

# 递归算法：1+2+3
def sum_num(num):
    print(num)  # 3 2 1
    if (num == 1):
        return 1
    temp = sum_num(num - 1)
    return temp + num


res = sum_num(3)
print(res)  # 6
