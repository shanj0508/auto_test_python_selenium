# -*- coding: utf-8 -*-
'''
    selenium grid模块的分布式部署
'''

# 通过grid模块创建浏览器驱动对象
# from selenium import webdriver
from time import sleep

from selenium.webdriver import Remote
import threading


# 引入多线程实现自动化测试效果
def open(driver):
    driver.get('http://www.baidu.com')
    sleep(5)
    driver.quit()


# 定义所有Node节点信息：M节点是不执行任务的，只需要写入所有的子节点信息即可。
hosts = {
    # 注册的第一个node节点的信息
    # 'http://192.168.65.35:4000/wd/hub': 'chrome',这是主节点，不需要写入。
    'http://192.168.65.35:5000/wd/hub': 'chrome',
    'http://192.168.65.35:6000/wd/hub': 'chrome'
}
# 创建线程组
th = []

# 基于节点创建浏览器对象
for host, browser in hosts.items():
    driver = Remote(command_executor=host, desired_capabilities={
        "platform": "Windows",
        "browserName": browser
    })
    # 将创建好的driver对象，创建对应的线程任务。
    th.append(threading.Thread(target=open, args=[driver]))

# 启动所有的已存线程
for t in th:
    t.start()
