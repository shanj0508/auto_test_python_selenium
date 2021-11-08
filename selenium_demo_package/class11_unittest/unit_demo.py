# -*- coding: utf-8 -*-
'''
    UnitTest测试框架的实操Demo
    语法规则：
        1.如果要UnitTest生效，需要让自定义类直接继承unittest.TestCase类
        2.UnitTest中的测试用例，都是以函数的形式存在。同时函数名需要以test开头，推荐使用test_开头
            -如果函数名称是以test开头的，则unittest认为这是一条测试用例，在执行时会执行该用例
            -如果函数不以test开头命名，就是普通函数，用于被测试用例调用才可以执行
        3.测试用例运行规则：
            -运行测试用例：必须在类中调用main函数，再在main函数中调用unittest.main()
            -如果不写main方法，则类中会默认调用main方法进行执行，但是为了规范，必须写上main方法
            -在类中基于编译器可以单独运行某一个测试用例，但是不推荐这样执行
        4.测试用例的执行顺序：
            -在UnitTets中有默认的用例执行顺序，这个顺序无法轻易改变，与测试用例的编写顺序无关。
            -默认用例执行顺序是根据ASCII码排序的：0-9  A-Z  a-z
        5.在UnitTest中，用例运行后，默认会强制关闭并结束driver进程。但是也会出现部分不清空的情况。
            所以，在用例结束后，需要在用例末尾加上quit函数，确保资源的释放。
        6.前置与后置：
            -前置与后置是固定写法，所有的前置与后置都是有且最多只能有一个
            -每个用例执行前都会运行一次setUp,执行后都会运行一次tearDown
            -所有的前置与后置，不参实际的测试行为，只做环境初始化与资源释放的操作。
            -对于多个用例的前置条件不统一的情况，用万能的setUp和tearDown，或者是通过管理手段（分成多个py文件来实现）
        7.前置后置级别：
            所有的前置后置都有等级存在，包括：
            class级别
                -class级别前置后置：必须通过装饰器@classmethod进行声明
                -class级别的前置后置通过cls定义类成员，通过self来调用
            method级别
                -method级别前置后置：每一条用例运行前会执行前置条件，运行后会执行后置

        8.类文件执行顺序：
            （1）main
            （2）继承于unittest.TestCase类的class
            （3）setUpClass：一个class对象仅执行一次
            （4）setUp：每个测试用例执行前都执行一次
            （5）测试用例
            （6）tearDown：每个测试用例执行后都执行一次
            （7）tearDownClass：一个class对象仅执行一次
        9.UnitTest中断言的调用
            以self.assert开头的所有方法都是断言





'''

# 导入unittest环境
import unittest
from selenium_demo_package.class11_unittest.web_keywordDriven import WebKey


# 自定义UnitTest类对象
class UnitDemo(unittest.TestCase):
    # 类前置 setUpClass：作用域是当前class
    @classmethod
    def setUpClass(cls):
        cls.wk = WebKey('Chrome')

    # 类后置  tearDownClass：作用域是当前class
    @classmethod
    def tearDownClass(cls):
        cls.wk.quit()

    # 前置 setUp  -> None:表示返回None的结果，即没有返回结果，也可以删除
    def setUp(self):
        pass

    # 后置 tearDown
    def tearDown(self):
        pass

    # 测试用例
    def test_case01(self):
        # wk = WebKey('Chrome')
        self.wk.visit('http://www.baidu.com')
        self.wk.input('id', 'kw', 'test1')
        self.wk.click('id', 'su')
        self.wk.sleep(2)
        # wk.quit()

    def test_case02(self):
        # wk = WebKey('Chrome')
        self.wk.visit('http://www.baidu.com')
        self.wk.input('id', 'kw', 'test2')
        self.wk.click('id', 'su')
        self.wk.sleep(2)
        # wk.quit()

    # test结尾
    def test_case03(self):
        self.wk.visit('http://www.baidu.com')
        self.wk.input('id', 'kw', 'test3')
        self.wk.click('id', 'su')
        self.wk.sleep(2)

    # 非test命名
    def case04(self):
        print('04')


# unittest中关于全局变量的定义和修改
class UnitDemo2(unittest.TestCase):
    # 定义全局变量的方式一:不推荐
    # temp = 'test'

    # 定义全局变量的方式二：
    @classmethod
    def setUpClass(cls):
        cls.temp = 'test'

    def test_case01(self):
        print('-----test_case01------')
        print(self.temp)
        # self的赋值方式用于在当前函数中改变变量的值，仅对函数内有效
        # self.temp = 'sss' + self.temp
        # 类名的赋值方式用于在class中改变变量的值，在函数外依旧有效
        # UnitDemo2.temp = 'sss' + self.temp
        self.temp = None
        print(self.temp)
        # 断言的调用
        # assertEqual(a, b)     a == b
        self.assertEqual(self.temp, 'test', msg='断言失败')
        # assertTrue(x) bool(x) is True
        # 这两行代码才是自定义关键字驱动封装在unittest中的完整的断言应用机制
        status = self.wk.assert_text()
        self.assertTrue(status, msg='断言失败')

    def test_case02(self):
        print('-----test_case02------')
        print(self.temp)


'''
输出结果1：
    -----test_case01------
    test
    ssstest
    -----test_case02------
    test
'''
'''
输出结果2：
    -----test_case01------
    test
    ssstest
    -----test_case02------
    ssstest
'''

# UnitTest运行
if __name__ == '__main__':
    unittest.main()
