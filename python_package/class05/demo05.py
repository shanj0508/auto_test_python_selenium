'''
函数：就是把具有独立功能的代码块，组织成一个小的模块
两个步骤：
    1.定义函数：封装成一个独立的功能
    2.调用函数：只有调用函数时，函数才被执行
函数的作用：函数只需要写一次，就可以多次调用，可以提高编码的效率，提高可复用性
函数的定义格式：
def 函数名(参数1,参数2,参数3,……):
    封装的代码
    return 返回值
函数的调用格式：函数名(参数1,参数2,参数3,……)
'''


# 定义函数
def func1():
    print('这是一个函数')


# 调用函数
func1()


# 例：两个数字求和
def sum():
    num1 = 10
    num2 = 20
    sum = num1 + num2
    print(f'和为：{sum}')


sum()


# 带参的函数
# 形参
def sum1(num1, num2):
    sum = num1 + num2
    print(f'{num1}+{num2}={sum}')


# 实参
sum1(30, 20)


# 参数的作用：针对不同的数据，进行相同的逻辑处理


# 函数的返回值 return
def sum2(num1, num2):
    return num1 + num2


# 调用函数，用变量接收函数执行的返回值
res = sum2(1, 2)
# 打印函数的返回值
print(res)


# 空函数
def empty():
    pass


# 函数的参数：位置参数(必需参数)，关键字参数，默认参数，可变参数(不定长参数)
#   位置参数：必须以正确的位置顺序传入参数，调用时的数量必须和声明时的一样。

# def person(name, age):
#     return '我是{}，今年{}岁'.format(name, age)
#
#
# person1 = person('小明', 18)
# print(person1)

#   关键字参数:函数调用使用关键字参数来确定传入的参数值,允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
#   允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
#   关键字参数可以扩展函数的功能。
# def person(name, age):
#     return '我是{}，今年{}岁'.format(name, age)
#
#
# person1 = person(age=18, name='小明')
# print(person1)

#   默认参数：调用函数时，如果没有传递参数，则会使用默认参数。默认参数降低了函数调用的难度。
#   注意：1.必选参数在前，默认参数在后
#        2.默认参数必须指向不变对象！
# def person(name='小红', age=19):
#     return '我是{}，今年{}岁'.format(name, age)
#
#
# # 调用时不传参数
# person1 = person()
# print(person1)  # 我是小红，今年19岁
# # 调用时传参，会覆盖默认参数的值
# person2 = person('小明', 18)
# print(person2)  # 我是小明，今年18岁
# person3 = person('小明')
# print(person3)  # 我是小明，今年19岁
# # 调用时不按顺序传参:必须把参数名写上
# person4 = person(age=18,name='小明')
# print(person4)  # 我是小明，今年18岁


# 声明函数时，如果位置参数和关键字参数同时存在，先写位置参数，再写默认参数

# def person(name, age=18):
#     return '我是{}，今年{}岁'.format(name, age)
#
#
# person1 = person('小明')
# print(person1)  # 我是小明，今年18岁
# person2 = person('小明',19)
# print(person2)  # 我是小明，今年19岁
# person3 = person(name='小明',age=20)
# print(person3)  # 我是小明，今年20岁


#   可变参数(不定长参数)：传入的参数个数是可变的，在定义的过程中不知道有多少个参数，就需要设置成不定长参数。
#   可以是1个、2个到任意个，还可以是0个。这些可变参数在函数调用时自动组装为一个tuple。
# *nums表示把nums这个list的所有元素作为可变参数传进去。
'''基本格式（两种）:
第一种格式：加了一个星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
   
第二种格式：加了两个星号 ** 的参数会以字典(dict)的形式导入。

def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
'''


#  * tuple元组形式
# def person(name, *args):
#     print(name, end='')
#     print(args)
#
#
# person('小明', 1, 2, 3)  # 小明(1, 2, 3)
# person('小明', 1, 2, 3, '小红')  # 小明(1, 2, 3, '小红')

# 声明函数时，参数中星号 * 可以单独出现，如果单独出现星号 * 后的参数必须用关键字传入。
# def sum(num1, num2, *, num3):
#     print('num1=', num1, end=',')
#     print('num2=', num2, end=',')
#     print('num3=', num3)
#     return num1 + num2 + num3
#
#
# res = sum(1, 2, num3=3)  # num1= 1,num2= 2,num3= 3
# print(res)  # 6

# ** dict字典形式,参数必须是字典形式
# def person(**kwargs):
#     print(kwargs)
#
#
# person(name='小明', age=18,gender='男')  # {'name': '小明', 'age': 18, 'gender': '男'}

# *和**同时存在
# def person(name, *args, **kwargs):
#     print(name, end=',')
#     print(args, end=',')
#     print(kwargs)
#
#
# # 调用时，不加关键字的参数以为()元组形式传入*args；加关键字的参数以{}字典形式传入 **kwargs
# person('小明', 1, 2, 3, age=18, gender='男')  # 小明,(1, 2, 3),{'age': 18, 'gender': '男'}

# 直接传入tuple和dict
# 例1：
# def person(*args, **kwargs):
#     print(args, end=',')
#     print(kwargs)
#
#
# tup1 = (1, '小明', 3.86)
# dic1 = {'name': '小红', 'age': 18, 'gender': '男'}
# # 自动将tup1, dic1以元组形式传入*args，而**kwargs为空字典{}
# person(tup1, dic1)  # ((1, '小明', 3.86), {'name': '小红', 'age': 18, 'gender': '男'}),{}
# 例2
# def person(*args, **kwargs):
#     print(*args, end=',')  # 这里的*会将传入的数据解析成元组的形式
#     print(**kwargs)  # 这里的**会将传入的数据解析成字典的形式
#
#
# tup1 = (1, '小明', 3.86)
# dic1 = {'name': '小红', 'age': 18, 'gender': '男'}
# # 分别将tup1, dic1传入*args和**kwargs
# person(tup1, dic1)  # (1, '小明', 3.86) {'name': '小红', 'age': 18, 'gender': '男'},

# 函数的嵌套
def test1():
    print('test1')
    print('+' * 50)


def test2():
    print('test2')
    print('-' * 50)
    test1()


test2()

# test2
# --------------------------------------------------
# test1
# ++++++++++++++++++++++++++++++++++++++++++++++++++


'''匿名函数：使用 lambda 来创建匿名函数。
lambda [arg1 [,arg2,.....argn]]:expression
'''
# # 匿名函数:通过lambda表达式来创建
# sum = lambda arg1, arg2: arg1 + arg2
#
# # 调用sum函数
# print("相加后的值为 : ", sum(10, 20))
# print("相加后的值为 : ", sum(20, 20))


# 模块：一个py文件就是一个模块
