# -*- coding: utf-8 -*-
'''
    UnitTest中的Skip装饰器应用
        共有四种不同的装饰器：
            1.@unittest.skip：用例执行时，无条件跳过该条用例
            2.@unittest.skipIf：当if条件为true时，执行跳过操作
            3.@unittest.skipUnless：当if条件为false时，执行跳过操作
            4.@unittest.expectedFailure：当用例报错时，系统选择忽略报错
'''

# 导入unittest环境
import unittest
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 自定义UnitTest类对象
class UnitDemo(unittest.TestCase):

    # 测试用例
    @unittest.skip('ignore')
    def test_case01(self):
        print('01')

    @unittest.skipIf(1 == 1, 'ignoreIf')
    def test_case02(self):
        print('02')

    @unittest.skipUnless(1 == 0, 'ignoreUnless')
    def test_case03(self):
        print('03')

    @unittest.expectedFailure
    def test_case04(self):
        self.assertEqual(1, 2, msg='断言失败')

    def test_case05(self):
        self.assertEqual(1, 2, msg='断言失败')


# UnitTest运行
if __name__ == '__main__':
    unittest.main()
