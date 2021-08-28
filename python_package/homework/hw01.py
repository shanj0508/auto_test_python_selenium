# 1、用print函数打印多个值
print(1, 2, 3)
print('hello world')
# 2、用print函数不换行打印
print(1, end='')
print(1)
# 3、导入模块的方式有哪些
'''
导入模块有三种方式：
方式一：
    导入：import 模块名    
    使用：模块名.函数名
方式二：
    导入：from 模块名 import 函数名1,函数名2,...,函数名n
    使用：直接用函数名
方式三：
    导入：from 模块名 import *    一次性导入模块下全部函数
    使用：直接用函数名
'''
import random

print("random:", random.randint(1, 3))

# 4、python有哪六种数据类型？不可变数据类型有哪些？可变数据类型有哪些？
'''
python的数据类型有6种，包括：
1.不可变数据类型：
    字符串 string
    数字 number
        int
        float
        bool:true false
    元组 tuple
2.可变数据类型：
    列表 list
    字典 dict
    集合 set
'''
# 5、分别对49.698作如下打印
num = 49.698
print(f'分别对{num}作如下打印')
# 1）四舍五入，保留两位小数
print('1）四舍五入，保留两位小数:', round(num, 2))
# 2）向上入取整
import math

print('2）向上入取整:', math.ceil(num))
# 3）向下舍取整
print('3）向下舍取整:', math.floor(num))
# print(int(num))
# 4）计算8除以5返回整型
print('4）计算8除以5返回整型:', 8 // 5)
print('4）计算8除以5返回浮点型:', 8 / 5)
# 5）求4的2次幂
print('5）求4的2次幂:', 4 ** 2)
# 6）返回一个（1, 100）随机整数
import random

print('6）返回一个（1, 100）随机整数:', random.randint(1, 100))
# 6、依次对变量a, b, c赋值为1, 2, 3
a = 1
b = 2
c = 3
print(a, b, c)
# 7、截取某字符串中从2索引位置到最后的字符子串
str2 = 'helloworld'
print(str2[2:])
# 8、对字符串“testcode”做如下处理：
str1 = 'testcode'
print('对字符串“testcode”做如下处理：')
# 1）翻转字符串
print('1）翻转字符串:', str1[::-1])
# 2）首字母大写
print('2）首字母大写:', str1.capitalize())
# 3）查找是否包含code子串，并返回索引值
print('3）查找是否包含code子串，并返回索引值:', str1.find('code'))
# 4）判断字符串的长度
print('4）判断字符串的长度:', len(str1))
# 5）从头部截取4个长度字符串
print('5）从头部截取4个长度字符串:', str1[0:4])
# 6）把code替换为123
print('6）把code替换为123:', str1.replace('code', '123'))
# 7）把“testcode”字符串中的两个单词转换为列表中的元素，并打印处理
print('7）把“testcode”字符串中的两个单词转换为列表中的元素，并打印处理:', list[str1[0:4], str1[4:]])

# 9、将小数转为整数
num1 = 3.14159
print(f'将小数{num1}转为整数:', int(num1))
# 10、如何打印出字符串“test\ncode”
print('test\ncode')
print('test\\ncode')
print(r'test\ncode')

# 11、按逗号分割列表当中的元素
list1 = [1, 2, 3, 4, 5, 6]
# 输出1，2，3，4，5，6
# list2 = []
# for i in list1:
#     list2.append(str(i))
# print("11题：", ",".join(list2))
# print("11题：", ",".join([str(l) for l in list1]))
for i in list1[:-1]:
    print(i, end=',')

print(list1[-1])

# 12、字符串"Hey, you - what are you doing here!?"分割成'Hey', 'you', 'what', 'are', 'you', 'doing', 'here'
str2 = "Hey, you - what are you doing here!?"
# res = str2.replace('-', '').split(' ')
res = ""
for c in str2:
    if c.isalpha() or c.isspace():
        res = res + c
print("12题：", '字符串分割：', res.split())
# 正则
import re

res = re.findall('\w+', str2)
print(res)  # ['Hey', 'you', 'what', 'are', 'you', 'doing', 'here']
