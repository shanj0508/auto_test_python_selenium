# -*- coding: utf-8 -*-
'''
    测试套件引用的unittest框架demo

'''

# 导入unittest环境
import unittest


# 自定义UnitTest类对象
class UnitDemo(unittest.TestCase):

    # 测试用例
    def test_case01(self):
        print('01')

    def test_case02(self):
        print('02')

    def test_case03(self):
        print('03')

    def test_case04(self):
        print('04')


# UnitTest运行
if __name__ == '__main__':
    unittest.main()
