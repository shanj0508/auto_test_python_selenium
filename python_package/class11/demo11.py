# 面向对象2
'''
私有的属性、私有的方法
面向对象的特征：封装、继承（重写）、多态
类方法、静态方法
'''

# 私有属性和私有方法
# 定义方法：属性名或方法名前加__表示是私有的
# class Person:
#     def __init__(self, name):
#         self.name = name
#         # 私有属性
#         self.__age = 18
#
#     # 私有方法
#     def __speak(self):
#         print('我叫%s,我今年%d岁！' % (self.name, self.__age))


# ming = Person('小明')
# # 私有属性和方法不能在外部直接调用，会报错
# print(ming.__age)  #AttributeError: 'Person' object has no attribute '__age'
# ming.__speak()  # AttributeError: 'Person' object has no attribute '__speak'

# 访问私有属性和私有方法：_类名__名称
# ming = Person('小明')
# print(ming._Person__age)  # 18
# ming._Person__speak()  # 我叫小明,我今年18岁！


# 面向对象的特征：封装、继承、多态
# 封装:把对象的细节封装起来，属性和方法封装到抽象类中，创建对象后可以调用对象中的属性和方法
'''
继承: 子类拥有父类的方法和属性，继承会沿继承链一直继承下去
作用：实现代码的重用
    单继承：
    多继承：
语法：class 子类名(父类名):
'''

# # 定义父类
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print('吃')
#
#     def sleep(self):
#         print('睡')
#
#     def run(self):
#         print('跑')
#
#
# # 定义子类 继承父类
# class Student(Person):
#     def study(self):
#         print('学习')
#
#
# ming = Student('小明', 30)
# # 子类可以直接使用父类的方法和属性
# print(ming.name, ming.age)
# ming.eat()
# ming.sleep()
# ming.run()
# ming.study()
# '''
# 小明 30
# 吃
# 睡
# 跑
# 学习
# '''
#
# hong = Student('小红', 18)
# print(hong.name, hong.age)
# hong.eat()
# hong.sleep()
# hong.run()
# hong.study()
# '''
# 小红 18
# 吃
# 睡
# 跑
# 学习
# '''


# 多继承：不建议使用

# 子类可以拥有多个父类，并且具有父类的所有属性和方法
# 语法：class 子类名(父类1,父类2,...,父类n):
# class ParentA:
#     def demoA(self):
#         print('demoA的方法')
#
#
# class ParentB:
#     def demoB(self):
#         print('demoB的方法')
#
#
# class ChildC(ParentA, ParentB):
#     def demoC(self):
#         print('demoC的方法')
#
#
# c = ChildC()
# c.demoA()
# c.demoB()
# c.demoC()

'''输出结果：
demoA的方法
demoB的方法
demoC的方法
'''

# 继承里面的重写
# 当父类的方法不能满足子类的需求时，就需要进行重写
# 重写就是直接覆盖父类的方法，在子类中重新编写
# class ParentA:
#     def demoA(self):
#         print('父类的demoA方法')
#
#
# class ChildB(ParentA):
#     def demoB(self):
#         print('子类ChildB的demoB的方法')
#
#     def demoA(self):
#         print('子类ChildB重写父类的demoA方法')
#
#
# class ChildC(ParentA):
#     def demoC(self):
#         print('子类ChildC的demoC的方法')
#
#
# c = ChildB()
# c.demoA()  # 子类ChildB重写父类的demoA方法
# c.demoB()  # 子类ChildB的demoB的方法
#
# c = ChildC()
# c.demoA()  # 父类的demoA方法
# c.demoC()  # 子类ChildC的demoC的方法

'''打印结果：
子类ChildB重写父类的demoA方法
子类ChildB的demoB的方法
父类的demoA方法
子类ChildC的demoC的方法
'''

# 继承里面的重载：在父类的方法基础上扩展功能，子类的方法包含父类的方法，又有子类的实现
# 语法：super().父类的方法名()
# 或者：父类名.方法(self)
#
# class Parent:
#     def demoA(self):
#         print('父类的demoA方法')
#
#
# class Child(Parent):
#     def demoB(self):
#         print('子类的demoB的方法')
#
#     def demoA(self):
#         # 调用父类的方法
#         # 写法一：
#         # super().demoA()
#         # 写法二：
#         Parent.demoA(self)
#
#         # 子类的实现
#         print('子类重载的实现')
#
#
# c = Child()
# c.demoA()
# c.demoB()

'''输出结果：
父类的demoA方法
子类重载的实现
子类的demoB的方法
'''

# 继承后，父类的私有属性，子类可以访问吗？不能访问

# class Parent:
#
#     def __init__(self):
#         self.name = '小明'
#         self.age = 18
#         # 父类的私有属性
#         self.__money = 500
#
#     def demoA(self):
#         print('父类的demoA方法')
#
#     # 父类的私有方法
#     def __saveMoney(self):
#         print('父类的私有方法方法')
#
#
# class Child(Parent):
#     def demoB(self):
#         print('子类的demoB的方法')
#
#
# c = Child()
# c.demoA()
# c.demoB()
# print(c.name)
# print(c.__money)

# 多态:指的是同一类型的对象调用同一个方法，表现不同的行为


# 类方法：想访问类里面的属性，调用类方法
# 语法：
#   定义：@classmethod cls
#   调用：类.方法()
# class Tool:
#     # 对象记录器
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         # 针对类属性做一个计数器
#         Tool.count += 1
#
#     def show_count(self):
#         print('工具对象的数量%d' % self.count)  # self表示当前调用类本身
#
#
# tool1 = Tool('刀子')
# print(tool1.count)
# tool1.show_count()
#
# tool2 = Tool('剪子')
# print(tool1.count)
# tool1.show_count()

'''输出结果:
1
工具对象的数量1
2
工具对象的数量2
'''


# 若我们想知道一共创建了多少个工具类，则不能通过self.count调用，需要通过类方法调用
# class Tool:
#     # 对象记录器
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         # 针对类属性做一个计数器
#         Tool.count += 1
#
#     @classmethod
#     def show_count(cls):
#         print('工具对象的数量%d' % cls.count)  # self表示当前调用类本身
#
#
# tool1 = Tool('刀子')
# tool2 = Tool('剪子')
# Tool.show_count()  # 工具对象的数量2


# 静态方法：staticmethod
class Person:
    @staticmethod
    # 注意：声明staticmethod后，定义的方法中没有self
    def run():
        print('静态方法run')


Person.run()  # 静态方法run

'''
类方法和静态方法都不需要实例化
    类方法: 
        @classmethod
        方法中自带cls,当方法内部只需要访问类属性时，可以使用类方法
    静态方法: 
        @staticmethod
        方法中没有self,当不需要访问实例对象的属性和类属性时，可以使用静态方法
若同时需要访问实例属性和类属性时，直接定义实例方法即可。
'''
