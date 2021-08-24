'''
数据类型：
    1.可变数据类型：
        -字典 dict
        -列表 list
        -集合 set
    2.不可变数据类型：
        -数字 number
            -整数 int
            -小数 float
            -bool: True 1   False 0
        -字符串 string
        -元组 tuple
打印数据类型：type()
'''
a = 1
print(a)
print(type(a))

'''
运算符：
    + - * / %取余 **乘方 //整除
'''

'''
比较符：
    == != <= >= <>   结果为True或False 
'''

'''
赋值运算符：
    = += -+ *= /=
'''

'''
数据类型转换：
 int()
 float()
'''

'''
数字的常用函数：
    绝对值函数：abs()
    ---下面两个函数需要导入math包才可以使用
    向上取整：ceil()
    向下取整：floor()
    ---
'''
a1 = -15
print(abs(a1))

import math

a2 = 12.3
print(math.ceil(a2))  # 向上取整

print(math.floor(a2))  # 向下取整

'''
保留几位小数：
    round(数字,保留位数)
'''
a3 = 3.141592653
print(round(a3, 3))

'''
随机数：
    random()  默认输出0-1之间的随机数
    randint(下限,上限)  输出给定区间的随机整数(这里是闭区间)
    导包快捷键alt+enter
'''
import random

print(random.random())  # 默认输出0-1之间的随机数
print(random.randint(0, 10))  # 输出0-10之间的随机整数

# 字符串：用单引号、双引号、三引号括起来   '字符串'  "字符串"  '''字符串'''
str1 = '小明'
str2 = "小红"
str3 = '''小丽'''
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))

# 字符串切片：将大的字符串切分成一个小的字符串
# str[开始索引:结束索引:步长]   区间是左闭右开的区间
# 开始索引默认从0开始
# 步长表示间隔，默认是1
# 索引为正数表示从左向右取值，索引为负数表示从右向左取值
str4 = 'python123'
print(str4)
# 输出thon
print(str4[2:6])
# 输出123
print(str4[6:9])
print(str4[6:])  # 结束索引缺省，表示取到最后一个字符
print(str4[-3:])

# 输出最后一个字符
print(str4[8])  # 正数表示从右向左取值
print(str4[-1])  # 负数表示从右向左取值

# 隔一个字符取一个：设置步长为2
print(str4[::2])

# 字符串的翻转：设置步长为-1
print(str4[::-1])

# 打印字符串的内存地址  id()
a = '123'
print(a, id(a))
a = '1234'
print(a, id(a))
# 可以看到上面两个a打印出来内存地址是不同的，因此其实是开辟了两个名为a的内存空间,
# 所以说字符串是不可变的数据类型,对a进行连续两次赋值，并没有改变原先a对应内存空间中的值，而是开辟了一个新的名为a的内存空间

# 字符串中的运算符  +拼接  *复制
str5 = 'hello'
str6 = 'world'
print(str5 + str6)
print(str5 * 2)

# 特殊字符   \n 换行  \t 制表符,可以进行缩进
print(str5 + '\n' + str6)
print('\t' + str5 + str6)

# \反斜杠 :
#   1.单独使用表示换行
str7 = 'aaaaa' \
       'aaaaaaa' \
       'aaaaa'
print(str7)
#   2.输出地址:r 或者\\
str8 = 'D:\github\auto_test_python_selenium\python_package\class02\demo01.py'
print(str8)

str9 = 'D:\\github\\auto_test_python_selenium\\python_package\\class02\\demo02.py'
print(str9)

str10 = r'D:\github\auto_test_python_selenium\python_package\class02\demo01.py'
print(str10)

# 字符串格式化
#    1.通过占位符进行占位：
#      %s 字符串  %d 数字类型  %f 浮点类型
print('你好，我叫%s，今年%d岁啦，我的体重是%f公斤。' % ('小红', 18, 48.5))
#    2.通过format格式占位
print('你好，我叫{}，今年{}岁啦，我的体重是{}公斤。'.format('小红', 18, 48.5))
#      format还可以指定传参顺序
print('你好，我叫{1}，今年{2}岁啦，我的体重是{0}公斤。'.format('小红', 18, 48.5))
#    3.f-string格式占位
name = '小红'
age = 18
weight = 48.5
print(f'你好，我叫{name}，今年{age}岁啦，我的体重是{weight}公斤。')

# 字符串的分割spilt
str11 = 'ab-c-def-g\nqwe-q\tdfd-fg'
print(str11.split())  # 默认分割空白  ['ab-c-def-g', 'qwe-q', 'dfd-fg']
print(str11.split('-'))  # 分割-  ['ab', 'c', 'def', 'g\nqwe', 'q\tdfd', 'fg']
print(str11.split('-', 1))  # 分割-,并且只分割一次  ['ab', 'c-def-g\nqwe-q\tdfd-fg']

# 字符串的连接join
str12 = '1'
str13 = 'abc'
print(str12.join(str13))  # 字符串str13用字符串12来连接

# 字符串的内置函数
#      替换 replace()
str14 = '小明'
print(str14.replace(str14, '小红'))

#      统计字符串的长度 len()
str15 = 'abcde12345'
print(len(str15))

#      查找字符串 find(str,开始索引,结束索引)
str16 = 'abcde12345'
print(str16.find('e'))
print(str16.find('e', 0))
print(str16.find('e', 10))  # 从索引为10的位置开始查找，如果没有找到目标字符串，返回 - 1

# 判断大小写  islower() isupper()
str17 = 'asdf'
print(str17.islower())  # 判断字符串是否由小写字母组成
print(str17.isalnum())  # 判断字符串是否由字母和数字组成
str18 = 'ASD'
print(str18.isupper())  # 判断字符串是否由大写字母组成
str19 = '123a'
str20 = u"23443434"
print(str19, str19.isnumeric())  # 判断字符串是否只由数字组成。这种方法是只针对unicode对象。
print(str20, str20.isnumeric())  # 判断字符串是否只由数字组成。这种方法是只针对unicode对象。

# 转换大小写 upper() lower() capitalize()
str21 = 'asdf'
print(str21.upper())
print(str21.capitalize())  # 首字母大写

str22 = 'ASD'
print(str21.lower())

# 元组tuple
# 定义：()来表示，数据是可以放任意类型的数据，数据之间用.隔开
# 创建一个空元组
tup1 = ()
print(tup1, type(tup1))  # () <class 'tuple'>
# 创建一个多个元素的元组
tup2 = (1, 2, 3, 'hello', True)
print(tup2)  # (1, 2, 3, 'hello', True)
# 创建一个仅有一个元素的元组，元素后必须加逗号,否则不是元组类型
tup3 = (1,)
print(tup3, type(tup3))  # (1,) <class 'tuple'>
# 若不加逗号，则不是元组类型，而是元素本来的数据类型
tup4 = (1)
print(tup4, type(tup4))  # 1 <class 'int'>
tup5 = ('hello')
print(tup5, type(tup5))  # hello <class 'str'>

# 访问元组中的数据,通过索引访问,索引从0开始
tup6 = (1, 2, 3, 'hello', True)
print(tup6[2])  # 3
print(tup6[3])  # hello
# 元组中使用切片
print(tup6[0:3])  # (1, 2, 3)
print(tup6[-1])  # True
# 元组不可以直接进行增加 删除和修改，因为是不可变数据类型
# 只能通过拼接的方式进行增加数据
tup7 = (1, 2, 3, 'hello', True)
tup8 = ('xiaohong',)
print(tup7 + tup8)  # (1, 2, 3, 'hello', True, 'xiaohong')
# 删除用del():注意，元组不支持一个元素的删除，只可以删除整个元组
# del tup7[1]  # 删除元组的第1个元素
# print(tup7)  # TypeError: 'tuple' object doesn't support item deletion
# del tup7  # 删除整个元组
# print(tup7)  # NameError: name 'tup7' is not defined  表示元组未定义，说明元组已经被删除成功

# 复制元组用*
tup9 = (1, 2, 3, 'hello', True)
print(tup9 * 2)  # (1, 2, 3, 'hello', True, 1, 2, 3, 'hello', True)

# 获取元组的长度
print(len(tup9))  # 5
