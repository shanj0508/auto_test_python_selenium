'''
    测试用例类：所有的测试代码都在该类实现
'''
import unittest
from time import sleep

from selenium import webdriver

from selenium_demo_package.class14_pom.page_object.cart_page import CartPage
from selenium_demo_package.class14_pom.page_object.login_page import LoginPage
from selenium_demo_package.class14_pom.page_object.phon_product_page import PhonePage


class Case(unittest.TestCase):
    # 前置条件
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.pp = PhonePage(cls.driver)
        cls.cp = CartPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 用例
    # def test_shopxo(self):
    #     user = 'shanjing'
    #     pwd = 'shanjing@.000'
    #     self.lp.login(user, pwd)
    #     count = '4'
    #     self.pp.add_cart(count)
    #     status = cp.cart_info(count)
    #     print('执行成功')
    #     print(status)
    #     sleep(5)
    #     self.driver.quit()
    # self.assertTrue(status)

    # 登录
    def test_01_login(self):
        user = 'shanjing'
        pwd = 'shanjing@.000'
        self.lp.login(user, pwd)

    # 添加商品
    def test_02_add_cart(self):
        count = '4'
        self.pp.add_cart(count)

    # 购物车校验
    def test_03_assert_cart(self):
        self.cp.cart_info()


if __name__ == '__main__':
    unittest.main()
