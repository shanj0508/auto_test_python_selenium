import os
import unittest
from HTMLTestReportCN import HTMLTestRunner

from selenium_demo_package.homework.my_conf.mail_conf import send_report

case_dir = './'
discover = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern='test_case*.py')

# 报告的保存路径
report_dir = './report/'
# 报告名称
report_file = report_dir + 'report.html'
# title
title = 'Demo系统的测试报告'
# description
description = '本次是V0.1版本的首轮冒烟测试执行结果'
# 判断报告路径是否存在，若路径不存在，则创建路径
if not os.path.exists(report_dir):
    os.mkdir(report_dir)
# 生成HTMLTestRunner测试报告相当于在文件中写入内容
with open(report_file, 'wb') as file:
    runner = HTMLTestRunner(stream=file, title=title,
                            description=description, verbosity=2, tester='陕璟')
    runner.run(discover)

# 发送邮件
send_report()
