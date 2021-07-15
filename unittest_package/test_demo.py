# coding=utf-8
# unittest测试框架应用
# 1、应用unittest框架：必须在类名继承：unittest.TestCase
# 2、运行测试用例：必须通过main函数运行
# 3、测试用例：所有的测试用例都是以函数的形式存在，函数的名称必须以test*开头。
# 4、用例加载顺序：UnitTest中有默认的用例加载顺序(根据ASCII码)：0-9  A-Z  a-z
# 5、所有的前置后置都有等级存在：class级别，method级别。前置与后置函数均有且只有一个
#       1)method级别前置后置：与用例管理，每一条用例运行前会执行前置条件，运行后会执行后置
#       2)cass级别前置后置：
#           a.必须定义装饰器@classmethod,
#           b.前置是在所有内容运行前运行一次，后置是在所有内容运行结束后运行一次
# 6、修改cls对象的值，在全局生效，需要通过类名.对象进行赋值操作才可以生效，而通过self.对象进行赋值只能够在当下函数中生效

# 导入unittest模块
import unittest
from selenium import webdriver
import time


# 应用unittest框架


class UnitDemo(unittest.TestCase):
    # 前置条件:class级别 应用场景：例如所有的配置
    @classmethod
    def setUpClass(self):
        pass
        # self.driver = webdriver.Chrome()
        # self.driver.get('https://www.baidu.com')

    # 前置条件:method级别
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        self.driver.maximize_window()

        # 测试用例：
    def test_search01(self):
        time.sleep(3)
        self.driver.find_element_by_id('kw').send_keys('python')
        self.driver.find_element_by_id('su').click()
        time.sleep(3)

    def test_search02(self):
        time.sleep(3)
        self.driver.find_element_by_id('kw').send_keys('java')
        self.driver.find_element_by_id('su').click()
        time.sleep(3)

    # 后置条件:method级别
    def tearDown(self):
        self.driver.quit()

    # 后置条件:class级别
    @classmethod
    def tearDownClass(cls):
        pass

        # 运行测试用例：
    if __name__ == '__main__':
        # UnitTest执行测试用例的行为
        unittest.main()
