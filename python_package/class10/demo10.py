# 面向对象1
'''
万物皆对象
面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。
OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
面向对象是在面向过程的基础上发展而来的
面向对象比面向过程更灵活，扩展性更好

面向过程 v.s. 面向对象

面向对象的两个核心内容：
    1.类：具有相同特征或者相同行为的事物的统称  （类的属性即特征，类的方法即行为）
    2.对象：

定义类：
class ClassName:
    属性：
    方法：
'''

# # 定义类
# class Cat:
#     # 类的属性
#     cat_color = '白色'
#     cat_weight = 20.8
#     cat_foot = 4
#
#     # 类的方法
#     def eat(self):
#         print('小猫爱吃鱼')
#
#     def catch(self):
#         print('小猫抓老鼠')
#
#
# # 类的实例化  变量名=类名()
# tom = Cat()
# # 类的使用   实例类.属性名  实例类.方法名
# print('tom.cat_color', tom.cat_color)  # tom.cat_color 白色
# tom.eat()  # 小猫爱吃鱼
# tom.catch()  # 小猫抓老鼠
# print('----------------------------')
# # 类的实例化
# jack = Cat()
# print('jack.cat_color', jack.cat_color)  # jack.cat_color 白色
# jack.eat()  # 小猫爱吃鱼
# jack.catch()  # 小猫抓老鼠
#
# print('----------------------------')
# # 默认打印16进制的内存地址
# print(tom)  # <__main__.Cat object at 0x000001B10969AFD0>
# # id()是十进制的内存地址
# print(id(tom))  # 1859878760400
# print(jack)  # <__main__.Cat object at 0x000001B10969AF70>
# print(id(jack))  # 1859878760304

# self的用法
# self代表的是对象本身,谁调用就是谁 相当于java中的this

# class Cat:
#     cat_color = '白色'
#     cat_weight = 20.8
#     cat_foot = 4
#
#     def eat(self):
#         print('%s小猫爱吃鱼' % self.cat_color)
#
#     def catch(self):
#         print('%s小猫抓老鼠' % self.name)
#
#
# tom = Cat()
# tom.name = 'tom'
# tom.cat_color = '黑色'
# tom.eat()  # 黑色小猫爱吃鱼
# tom.catch()  # tom小猫抓老鼠
#
# print('----------------------------')
#
# jack = Cat()
# jack.name = 'jack'
# jack.eat()  # 白色小猫爱吃鱼
# jack.catch()  # jack小猫抓老鼠

# 属性在方法中的写法
# init函数：是一个内置方法，专门用来定义一个类具有哪些属性的方法  类似于java中的构造函数
# 特点:创建对象时自动调用
# init方法内部使用：self.属性名 = 属性初始值

# class Cat:
#     # 初始化函数init
#     def __init__(self):
#         print('这是一个初始化函数')
#         # 定义属性
#         self.name = 'tom'
#         self.color = '白色'
#
#     def eat(self):
#         print('%s爱吃鱼' % self.name)
#
#
# # 只要创建了实例化对象，就会执行init函数
# tom = Cat()  # 这是一个初始化函数
# tom.eat()  # tom爱吃鱼
#
# print('----------------------------')
#
# jack = Cat()  # 这是一个初始化函数
# jack.eat()  # tom爱吃鱼

# init函数里面有参数，必须传参数，实例化对象时传参
# class Cat:
#     # 初始化函数init
#     def __init__(self, name, color):
#         print('这是一个初始化函数')
#         # 定义属性
#         self.name = name
#         self.color = color
#
#     def eat(self):
#         print('%s爱吃鱼,是%s' % (self.name, self.color))
#
#
# # 只要创建了实例化对象，就会执行init函数
# tom = Cat('tom', '白色')  # 这是一个初始化函数
# tom.eat()  # tom爱吃鱼,是白色
#
# print('----------------------------')
#
# jack = Cat('jack', '黑色')  # 这是一个初始化函数
# jack.eat()  # jack爱吃鱼,是黑色

'''内置函数(了解)
__init__ : 创建实例化对象时自动调用
__del__ : 对象从内存中销毁之前，会被自动调用
__str__ : 返回对象的描述信息 print函数输出
'''


class Cat:
    # 初始化函数init
    def __init__(self, name):
        self.name = name
        print('%s被创建了' % self.name)

    def __del__(self):
        print('%s被销毁了' % self.name)

    def __str__(self):
        return '%s是一只小猫' % self.name

print('-' * 50)
# 创建实例化对象
tom = Cat('tom')
# 打印str函数的描述信息
print(tom)
# 删除对象
del tom
print('-' * 50)
#


'''打印结果：
--------------------------------------------------
tom被创建了
tom是一只小猫
tom被销毁了
--------------------------------------------------
'''
