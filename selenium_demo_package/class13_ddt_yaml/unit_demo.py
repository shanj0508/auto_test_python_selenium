'''
    基于DDT实现的UnitTest的数据驱动应用
'''
# 导入unittest环境
import unittest
from selenium_demo_package.class13_ddt_yaml.my_conf.web_keywordDriven import WebKey
from ddt import ddt, data, unpack,file_data


# 文件的内容读取
# def read_file():
#     li = []
#     file = open('./data/data.txt', 'r', encoding='utf-8')
#     for line in file.readlines():
#         li.append(line)
#     return li


# 自定义UnitTest类对象
@ddt  # 声明该class类将要调用ddt模块进行数据管理。
class UnitDemo(unittest.TestCase):
    def setUp(self):
        self.wk = WebKey('Chrome')

    def tearDown(self):
        self.wk.quit()

    # 测试用例
    '''
        data执行的操作是一个拆包的行为。
        @data('test1', 'test2', 'test3') 
        将所有的数据以逗号进行分割：
             test1
             test2
             test3
         分割后基于拆分出来的结果总数，定义循环次数。每次循环传入一个参数进去。
         
        
    '''

    # 传入1个参数
    # @data('test1', 'test2', 'test3')
    # def test_case01(self, name):
    #     self.wk.visit('http://www.baidu.com')
    #     self.wk.input('id', 'kw', name)
    #     self.wk.click('id', 'su')
    #     self.wk.wait('xpath', '//*[@id="1"]')
    #     self.wk.sleep(3)

    # 传入2个参数:可以以元组、list、dict的形式传参
    # 元组
    # @data(('http://www.baidu.com', 'test1'),
    #       ('http://www.baidu.com', 'test2'),
    #       ('http://www.baidu.com', 'test3'))  # 这里的参数书写顺序与变量顺序一一对应
    # list
    # @data(['http://www.baidu.com', 'test1'])
    # dict
    # @data({'url': 'http://www.baidu.com', 'name': 'test1'})
    # @unpack  # 二次解包   按照参数顺序依次传入，因此只能传递定长参数
    # def test_case01(self, url, name):
    #     self.wk.visit(url)
    #     self.wk.input('id', 'kw', name)
    #     self.wk.click('id', 'su')
    #     self.wk.wait('xpath', '//*[@id="1"]')
    #     self.wk.sleep(3)

    # 基于文件的内容读取，实现数据驱动
    # @data(*read_file())
    # def test_case01(self, txt):
    #     url = txt.split(',')[0]
    #     name = txt.split(',')[1]
    #     self.wk.visit(url)
    #     self.wk.input('id', 'kw', name)
    #     self.wk.click('id', 'su')
    #     self.wk.wait('xpath', '//*[@id="1"]')
    #     self.wk.sleep(3)

    # 基于yaml文件的内容读取，实现数据驱动
    '''
        通过@file_data()读取的所有内容，传入kwargs参数
    '''
    @file_data('./data/test_data.yaml')
    def test_case01(self, **kwargs):
        self.wk.visit(kwargs['url'])
        self.wk.input(**kwargs['input'])
        self.wk.click(**kwargs['click'])
        self.wk.sleep(3)

    # def test_case01(self):
    #     self.wk.visit('http://www.baidu.com')
    #     self.wk.input('id', 'kw', 'test1')
    #     self.wk.click('id', 'su')
    #     self.wk.wait('xpath', '//*[@id="1"]')
    #     self.wk.sleep(3)
    #
    # def test_case02(self):
    #     self.wk.visit('http://www.baidu.com')
    #     self.wk.input('id', 'kw', 'test2')
    #     self.wk.click('id', 'su')
    #     self.wk.wait('xpath', '//*[@id="1"]')
    #     self.wk.sleep(3)
    #
    # def test_case03(self):
    #     self.wk.visit('http://www.baidu.com')
    #     self.wk.input('id', 'kw', 'test3')
    #     self.wk.click('id', 'su')
    #     self.wk.wait('xpath', '//*[@id="1"]')
    #     self.wk.sleep(3)


# UnitTest运行
if __name__ == '__main__':
    unittest.main()
