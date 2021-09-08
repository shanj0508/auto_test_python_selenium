# 装饰器
'''
装饰器：给已有的函数增加额外的功能，它的本质是一个闭包函数。

闭包函数：
    闭包定义：在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，我们把这个使用外部函数变量的内部函数称为闭包。
    形成条件：
        1.实现函数嵌套
        2.内部函数使用外部函数的变量
        3.外部函数返回内部函数名（函数名后不加括号）
    作用：闭包可以保存外部函数的变量，直接给内部函数去调用，不会因为外部函数调用结束而销毁
'''

# 简单的闭包实现
# 外部函数
# def test1(a):
#     age = 10
#
#     # 内部函数
#     def test2():
#         # 内部函数使用外部函数的变量
#         print(a, age)
#
#     # 外部函数返回内部函数
#     return test2
#
#
# res = test1('a')
# res()  # a 10

# 定义外部函数
# def add_x(num1):
#     print('num1:', num1)
#
#     def add_y(num2):
#         sum = num1 + num2
#         print('结果是：', sum)
#
#     return add_y
#
#
# a = add_x(3)
# a(2)

'''打印结果：
num1: 3
结果是： 5
'''

# 定义外部函数
# def config_name(name):
#     def say_name(info):
#         print(name + ':' + info)
#
#     return say_name
#
#
# a = config_name('小红')
# a('我是女生')
# b = config_name('小明')
# b('我是男生')

'''打印结果：
小红:我是女生
小明:我是男生
'''

'''
装饰器：给已有的函数增加额外的功能，它的本质是一个闭包函数。
特点：
    1.不修改已有函数的源代码
    2.不修改已有函数的调用方式
    3.给已有函数增加额外的功能
'''

# 装饰器里面的参数是函数
# # 装饰器的简单实现
# def check(fn):
#     print('装饰器函数执行了')
#
#     def inner():
#         print('请先登录')
#         fn()
#
#     return inner
#
#
# def comment():
#     print('发表评论功能')
#
#
# # 运行方式
# a = check(comment)
# a()
'''运行结果：
装饰器函数执行了
请先登录
发表评论功能
'''


# 装饰器的语法糖写法 @方法名
# 装饰器的简单实现
def check(fn):
    print('装饰器函数执行了')

    def inner():
        print('请先登录')
        fn()

    return inner


@check
def comment():
    print('发表评论功能')


# 运行方式
# a = check(comment)
# a()
comment()
# TODO：comment=inner??
# 上面代码执行过程：
# 运行comment()，执行comment函数之前会先找到装饰器@check，然后执行check函数，打印'装饰器函数执行了'
# check函数执行完成后返回inner，所以此时comment==inner(),执行inner函数，打印'请先登录'
# fn==comment()，执行fn()函数，打印'发表评论功能'


'''运行结果：
装饰器函数执行了
请先登录
发表评论功能
'''
