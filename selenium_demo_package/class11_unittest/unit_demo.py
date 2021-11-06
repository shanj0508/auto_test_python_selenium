'''
    UnitTest测试框架的实操Demo
    语法规则：
        1.如果要UnitTest生效，需要让自定义类直接继承unittest.TestCase类
        2.UnitTest中的测试用例，都是以函数的形式存在。同时函数名需要以test开头，推荐使用test_开头
            -如果函数名称是以test开头的，则unittest认为这是一条测试用例，在执行时会执行该用例
            -如果函数
        3.测试用例运行规则：
            -运行测试用例：必须在类中调用main函数，再在main函数中调用unittest.main()
            -如果不写main方法，则类中会默认调用main方法进行执行，但是为了规范，必须写上main方法
            -在类中基于编译器可以单独运行某一个测试用例，但是不推荐这样执行



'''

# 导入unittest环境
import unittest


# 自定义UnitTest类对象
class UnitDemo(unittest.TestCase):
    # 测试用例
    def test_case01(self):
        print('01')
        self.case04()

    def test_case02(self):
        print('02')

    # test结尾
    def case03_test(self):
        print('03')

    # 非test命名
    def case04(self):
        print('04')


# UnitTest运行
if __name__ == '__main__':
    unittest.main()
