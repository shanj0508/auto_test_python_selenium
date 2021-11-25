#导入unittest模块
import unittest

#要应用unittest框架，必须在类名中继承unittest.TestCase
class UnitDemo(unittest.TestCase):
    def test_login(self):
        print("这是login函数")
        self.assertEqual("123","123",msg='断言失败')

if __name__ == '__main__':
    # unittest执行测试用例的行为
    unittest.main()