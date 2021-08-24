# python 流程控制
'''
条件判断语句: if

if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3

'''

# 例1：如果年龄大于18，允许进入网吧，否则回家做作业
# age = 19
# age = int(input('请输入你的年龄：'))
# print(age, type(age))
# if age >= 18:
#     print(f'你已经{age}岁了，可以进入网吧')
# else:
#     print('你才%d岁，快回家写作业吧' % (age))

# 例2：成员运算符 in  和 not in
# str1 = 'hello'
# if 'o' in str1:
#     print('yes!!!')
# elif 'o' not in str1:
#     print('no!!!')

# 例3：身份运算符 is 和 is not
# a = 'hello'
# a = 'world'
# if id(a) is id(a):
#     print('两个a的地址相同')
# elif id(a) is not id(a):
#     print('两个a的地址不相同')

'''
多重if嵌套：

if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句

'''
# 例4:多重if嵌套
# score = int(input('请输入成绩：'))
# if score >= 90:
#     print(f"你的成绩是：{score}，优秀！")
# elif score >= 80:
#     print(f'你的成绩是：{score}，良好！')
# elif score >= 70:
#     print(f'你的成绩是：{score}，中等')
# elif score >= 60:
#     print(f'你的成绩是：{score}，及格')
# else:
#     print(f'你的成绩是：{score}，不及格')

# score = int(input('请输入成绩：'))
# if score >= 60:
#     print('考试通过！')
#     if score >= 90:
#         print('你的成绩是{},优秀！'.format(score))
#     elif score >= 70:
#         print('你的成绩是{},良好！'.format(score))
#     else:
#         print('你的成绩是{},一般！'.format(score))
# else:
#     print('考试不通过！,你的成绩是{}'.format(score))
# 循环语句：for  和  while
'''
循环语句：while

while 判断条件(condition)：
    执行语句(statements)……
    
注意：在 Python 中没有 do..while 循环。
'''
# 例1： 打印5次hello world
# i = 1
# while i <= 5:
#     print('hello world %d' % (i))
#     i += 1  # python中没有i++

# 例2：0到100的数字求和
# i = 0
# sum = 0
# while i <= 100:
#     print('i:', i)
#     sum += i;
#     print('sum:', sum)
#     i += 1;
#
# print('0-100的和为：', sum)

'''
while 循环使用 else 语句:如果while中有break或者continue,那么就不会执行else中的语句

while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
'''
# i = 0
# sum = 0
# while i <= 100:
#     print('i:', i)
#     sum += i;
#     print('sum:', sum)
#     i += 1;
# else:
#     print('0-100的和为：', sum)

# while嵌套循环
'''
例：打印星星
*
**
***
****
*****
'''
# row = 1
# while row <= 5:
#     cols = 1
#     while cols < row:
#         print('*', end='')
#         cols += 1
#     print('*')
#     row += 1
'''
循环语句：for

for <variable> in <sequence>:
    <statements>
else:
    <statements>
    
注意： <sequence>表示集合：元组、列表、字典
'''
# 例1： 打印5次hello world
# for i in range(5):
#     print('hello world %d' % (i))
# 例2：打印list
# list1 = ['阿大', '阿二', 1, 2, 3]
# for item in list1:
#     print(item)
# 例3：0到100的数字求和
# sum = 0
# for i in range(101):
#     sum += i
#     print(i)
#     print(sum)


# range()函数：生成数字序列
# for i in range(5):
#     print(i)
# range()函数：指定区间值 左闭右开
# for i in range(5, 9):
#     print(i)
# range()函数：设置步长
# for i in range(1, 10, 2):
#     print(i)
# range()函数：负数
# for i in range(-10, -1, 2):
#     print(i)


# for嵌套循环
'''
例：打印星星
*
**
***
****
*****
'''
for i in range(0, 5):
    for j in range(0, i):
        print('*', end='')
    print('*')
'''
break和continue：
break : 跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
continue : 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

'''
# 例：打印0-9的数字，循环到3时跳出循环
# break
# i = 0
# while i < 10:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# continue
# i = 0
# while i < 10:
#     if i == 3:
#         i += 1  # continue中必须加可执行的语句
#         continue
#     print(i)
#     i += 1
