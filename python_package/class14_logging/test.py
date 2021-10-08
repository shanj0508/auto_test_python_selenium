from python_package.class14_logging.basePagefb import BasePage
from selenium import webdriver

driver=BasePage(webdriver.Chrome())
driver.open('http://www.baidu.com')
driver.on_input('id','kw','秋水')
driver.on_click('id','su')
driver.wait(3)
driver.on_click('xpath','//*[@id="1"]/h3/a/em')
driver.wait(3)
driver.close()



# 日志体现在哪
# import os
# import re


# def find_log(path):
#   file_list = os.listdir(path)
#   for file in file_list:
#     file_name = file
#     log_path = os.path.join(path, file)
#     with open(log_path, 'rb') as f:
#       lines = f.readlines()
#       index = 0
#       for line in lines:
#         index += 1
#         if 'Crash' in line.decode("utf8", "ignore") or 'ERROR' in line.decode("utf8", "ignore"):
#           ss = re.findall(r'(.*Crash.*)', line.decode("utf8", "ignore"))
#           zz = re.findall(r'(.*ERROR.*)', line.decode("utf8", "ignore"))
#           if len(zz) > 0:
#             with open('result.txt', 'a',encoding='utf-8') as ff:
#               ff.write('文件名：'+file_name + ' 第' + str(index) + '行： ' + zz[0] + '\n')
#           elif len(ss) > 0:
#             with open('result.txt', 'a') as ff:
#               ff.write('文件名：'+file_name + ' 第' + str(index) + '行： ' + ss[0] + '\n')
#           else:
#             break
# a=find_log(r'D:\newclass\logdemo\logs')
# print(a)

