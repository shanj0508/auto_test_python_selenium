import unittest

from selenium_demo_package.homework.my_conf.web_keywordDriven import WebKey


class UnitTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.wk = WebKey('Chrome')
        cls.num = '4'
        cls.temp = 'test'

    @classmethod
    def tearDownClass(cls) -> None:
        cls.wk.quit()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # 测试用例1:实现电商的登录
    def test_login(self):
        self.wk.visit('http://39.98.138.157/shopxo/')
        self.wk.click('link text', '登录')
        self.wk.wait('xpath', '//*[text()="还没有帐号？"]')
        self.wk.input('name', 'accounts', 'shanjing')
        self.wk.input('name', 'pwd', 'shanjing@.000')
        self.wk.click('xpath', '//button[text()="登录"]')
        self.wk.wait('xpath', '//*[text()="登录成功"]')
        # 断言
        status = self.wk.assert_text('link text', '退出', '退出')
        self.assertTrue(status, msg='断言失败')

    # @unittest.expectedFailure
    def test_case01(self):
        print('-----test_case01------')
        print(self.temp)
        self.temp = 'sss' + self.temp
        print(self.temp)
        self.assertEqual(self.temp, 'test', msg='断言失败')

    # @unittest.skip('无条件忽略此用例')
    def test_case02(self):
        print('-----test_case02------')
        print(self.temp)
        self.assertEqual(self.temp, 'test', msg='断言失败')

    def test_visit01(self):
        self.wk.visit('http://www.baidu.com')
        self.wk.input('id', 'kw', 'test1')
        self.wk.click('id', 'su')
        self.wk.sleep(2)

    def test_visit02(self):
        self.wk.visit('http://www.baidu.com')
        self.wk.input('id', 'kw', 'test2')
        self.wk.click('id', 'su')
        self.wk.sleep(2)

    def test_visit03(self):
        self.wk.visit('http://www.baidu.com')
        self.wk.input('id', 'kw', 'test3')
        self.wk.click('id', 'su')
        self.wk.sleep(2)


if __name__ == '__main__':
    unittest.main()
