# 文件处理：
'''
文件类型：
    1.txt文件
    2.csv文件
    3.xml文件
    4.excel文件
    5.yaml文件
'''

#     一.txt文件
'''
文件的基本操作：
    1.打开文件:open(文件路径，访问模式)  with open() as 别名
    2.读取文件：文件对象.read()    read()   readline()  readlines()
    3.写入文件: 文件对象.write('文件内容')
    4.关闭文件：文件对象.close()  避免占用服务器资源
'''
# 1.打开文件
# f1 = open('file1.txt', 'r', encoding='utf-8')
# 2.读取文件
# print('read():\n', f1.read())
'''输出结果：
1,小明,10,男
2,小红,11,女
3,小芳,12,女
4,xiaoming,13,男
5,xiaohong,14,女
'''
# print('readline():\n', f1.readline())  # 输出结果： 1,小明,10,男
# print('readlines():\n', f1.readlines())
# 输出结果： ['1,小明,10,男\n', '2,小红,11,女\n', '3,小芳,12,女\n', '4,xiaoming,13,男\n', '5,xiaohong,14,女']

# 把列表中的数据都读取出来
# for i in f1.readlines():
#     print(i)

'''输出结果：
1,小明,10,男

2,小红,11,女

3,小芳,12,女

4,xiaoming,13,男

5,xiaohong,14,女

Process finished with exit code 0

'''

# 把列表中的名字都读取出来
# for i in f1.readlines():
#     # print(i)
#     # print(type(i))  # <class 'str'>
#     # print(i.split(','))  # 用逗号分割字符串，分割后返回一个列表
#     # print(type(i.split(',')))  # <class 'list'>
#     print(i.split(',')[1])  # 通过列表的下标读取姓名
#     '''输出结果：
#         小明
#         小红
#         小芳
#         xiaoming
#         xiaohong
#     '''


# with open() as 别名
# 把列表中的名字和年龄都读取出来
# with open('file1.txt', 'r+', encoding='utf-8') as f1:
#     a = f1.readlines()
#     print(a)  # ['1,小明,10,男\n', '2,小红,11,女\n', '3,小芳,12,女\n', '4,xiaoming,13,男\n', '5,xiaohong,14,女']
#
# for i in a:
#     print(i)
#     print(i.split(','))
#     print(i.split(',')[1:3])

# 3.写入文件
# f1.write('这是写入的文件')
# 4.关闭文件
# f1.close()


#     二.csv文件：csv本质上也是一种文本，文本内容以逗号.隔开,  存储方式：excel表格文件存储
#     表格相关的包：openpyxl,pandas,xlrd

# 读取csv文件需要先导包
import csv

#
# #    1.打开文件:open(文件路径，访问模式)  with open() as 别名
# f2 = open('file2.csv', 'r', encoding='utf-8')
# #    2.读取文件：csv.reader(文件对象)   返回一个文件对象，可以通过for循环获取文件对象的数据
# a = csv.reader(f2)
# print(a)  # <_csv.reader object at 0x0000016BFAEE7C40>
#
# for i in a:
#     print(i)
#     '''输出结果：
#         ['1', '小明', '10', '男']
#         ['2', '小红', '11', '女']
#         ['3', '小芳', '12', '女']
#         ['4', 'xiaoming', '13', '男']
#         ['5', 'xiaohong', '14', '女']
#     '''
#     print(i[1])  # 获取名字
# #    4.关闭文件：文件对象.close()  避免占用服务器资源
# f2.close()

# with open() as 别名
# with open('file2.csv', 'r', encoding='utf-8') as f2:
#     a = f2.readlines()
#     print(a)  # ['1,小明,10,男\n', '2,小红,11,女\n', '3,小芳,12,女\n', '4,xiaoming,13,男\n', '5,xiaohong,14,女']
# for i in a:
#     # print(i)
#     # print(type(i))
#     print(i.split(',')[1])  # 获取名字


#    3.写入文件: csv.write('文件内容')
# student1 = [6, '小花', 15, '女']
# student2 = [7, 'xiaoli', 16, '男']
# f2 = open('file2.csv', 'a', encoding='utf-8',newline='')
# write1 = csv.writer(f2, dialect='excel')  # 以excel的格式写入
# write1.writerow(student1)  # 写入csv文件的具体数据student1
# write1.writerow(student2)  # 写入csv文件的具体数据student2


#     三.xml文件：类似html
# 读取xml文件需要先导包
from xml.dom import minidom

# TODO
# 在dom 及 minidom 下有红色波浪线报错
# 报错内容为：Cannot find reference 'dom' in '__init__.pyi'
# Unresolved reference 'minidom'
# ‘No module named dom’

#    1.加载xml文件: minidom.parse(文件路径)
# dom = minidom.parse('file3.xml')
#    2.读取文件：文件对象.documentElement
# root = dom.documentElement
# 获取根节点
# print(root.nodeName)  # Class
# 获取根节点类型
# print(root.nodeType)  # 1：表示节点
# 获取标签 name和age  getElementsByTagName
# name1 = root.getElementsByTagName('name')
# print(name1[0].nodeName)  # name
# age1 = root.getElementsByTagName('age')
# print(age1[0].nodeName)  # age
# 获取标签里面的值 firstChild.data
# name1 = root.getElementsByTagName('name')
# print(name1[0].firstChild.data)  # 小明
# age1 = root.getElementsByTagName('age')
# print(age1[0].firstChild.data)  # 10
# 获取属性值：getAttribute
# input1 = root.getElementsByTagName('input')
# user = input1[0].getAttribute('username')
# print(user)  # student
#    3.写入文件: 文件对象.write('文件内容')
#    4.关闭文件：文件对象.close()  避免占用服务器资源

# 题目:一次获取所有学生的信息
# dom = minidom.parse('file3.xml')
# root = dom.documentElement
# stus = root.getElementsByTagName('student')
# print(stus)  # [<DOM Element: student at 0x298991f90d0>, <DOM Element: student at 0x29899205f70>]
# name1 = root.getElementsByTagName('name')
# age1 = root.getElementsByTagName('age')
# gender1 = root.getElementsByTagName('gender')
#
# for i in range(2):
#     print(name1[i].firstChild.data)
#     print(age1[i].firstChild.data)
#     print(gender1[i].firstChild.data)
#     '''输出结果:
#         小明
#         10
#         男
#         小红
#         11
#         女
#     '''
# 题目：只拿sid="S001"的值
dom = minidom.parse('file3.xml')
root = dom.documentElement
stus = root.getElementsByTagName('student')
for i in stus:
    # print(i.getAttribute('sid'))
    if i.getAttribute('sid') == 'S001':
        print('sid:S001')
        name1 = i.getElementsByTagName('name')[0]
        print('name:', name1.firstChild.data)

#     四.excel文件

#    1.打开文件:open(文件路径，访问模式)  with open() as 别名
#    2.读取文件：文件对象.read()    read()   readline()  readlines()
#    3.写入文件: 文件对象.write('文件内容')
#    4.关闭文件：文件对象.close()  避免占用服务器资源
#     五.yaml文件


#    1.打开文件:open(文件路径，访问模式)  with open() as 别名
#    2.读取文件：文件对象.read()    read()   readline()  readlines()
#    3.写入文件: 文件对象.write('文件内容')
#    4.关闭文件：文件对象.close()  避免占用服务器资源
