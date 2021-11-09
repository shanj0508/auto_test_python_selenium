# -*- coding: utf-8 -*-
'''
    测试套件的应用
'''
import os
import unittest
# from HTMLTestRunner import HTMLTestRunner
from HTMLTestReportCN import HTMLTestRunner
from selenium_demo_package.class12_suite_runner.unit_demo import UnitDemo


# 创建套件
# suite = unittest.TestSuite()

# 1.添加测试用例到套件
# 1.1 添加单个测试用例：通过测试用例的名称来添加
# suite.addTest(UnitDemo('test_case02'))
# suite.addTest(UnitDemo('test_case01'))
# suite.addTest(UnitDemo('test_case03'))

# 1.2 添加多个测试用例：通过list来实现
# cases = [UnitDemo('test_case02'), UnitDemo('test_case01'), UnitDemo('test_case03')]
# suite.addTests(cases)

# 1.3 添加多个测试用例：通过添加整个UnitTest类来实现
# 注：以类的方式添加测试用例后，测试用例的执行顺序是UnitTest默认顺序，而不是用例编写顺序。
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(UnitDemo))

# 1.4 添加多个测试用例：通过Name来实现
# 直接传入类名会报错
# suite.addTests(unittest.TestLoader().loadTestsFromName('UnitDemo'))
# 报错：ImportError: No module named UnitDemo
# 必须以文件名或文件名.类名的格式传入类名，不能直接以类名的方式传入
# suite.addTests(unittest.TestLoader().loadTestsFromName('unit_demo'))
# suite.addTests(unittest.TestLoader().loadTestsFromName('unit_demo.UnitDemo'))

# 1.5 添加多个测试用例：通过文件名批量添加
# (1)定义用例的路径
case_dir = './'
# (2)基于路径来获取用例，组成套件
# discover返回值就是一个套件，所以不需要创建套件
discover = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern='u*.py')

# 套件的运行：一定要结合运行器来实现
# 2.创建默认的运行器:TextTestRunner
# verbosity是日志等级，值包括：0,1,2
# runner = unittest.TextTestRunner(verbosity=2)
# 3.基于运行器来执行套件
# runner.run(suite)
# runner.run(discover)

# 基于HTMLTestRunner运行器生成测试报告
# 基本的报告配置

# 报告的保存路径
report_dir = './report/'
# 报告名称
report_file = report_dir + 'report.html'
# 判断报告路径是否存在，若路径不存在，则创建路径
if not os.path.exists(report_dir):
    os.mkdir(report_dir)
# 生成HTMLTestRunner测试报告相当于在文件中写入内容
with open(report_file, 'wb') as file:
    runner = HTMLTestRunner(stream=file, title='测试报告title',
                            description='测试报告description', verbosity=2)
    runner.run(discover)
