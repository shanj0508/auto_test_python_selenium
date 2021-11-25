# -*- coding: utf-8 -*-
'''
    python的多线程实现。
    通过调用threading模块来实现多线程的建立。每一条线程都是独立的，彼此之间不会存在干扰。
    但是在python体系下，多线程受到内存的影响，部分情况会存在问题。
    多线程不是并发，只是在极短的时间内启动，每一条线程的启动都会存在时间差，只是比较短而已。
'''
import threading
from time import sleep

from selenium import webdriver


# def fun_01():
#     for i in range(5):
#         print('01')
#         sleep(3)


# 单线程运行
# fun_01()

# 引入多线程的机制
# thread = threading.Thread(target=fun_01)
# thread.start()

# for i in range(5):
#     print('非线程:{}'.format(i))
#     sleep(3)

# 引入多线程实现自动化测试效果
def open(driver):
    driver.get('http://www.baidu.com')
    sleep(5)
    driver.quit()


# open(webdriver.Chrome())

# 定义线程组
th = []

driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver3 = webdriver.Chrome()

# 引入threading模块
# 创建一个线程threading.Thread
th.append(threading.Thread(target=open, args=[driver1]))
th.append(threading.Thread(target=open, args=[driver2]))
th.append(threading.Thread(target=open, args=[driver3]))

# 所有的线程都需要被手动调用执行
for t in th:
    # 启动线程
    t.start()
    # 等待当前线程内容执行完成再运行后续线程，就相当于变成了单线程
    '''
        如果多条线程对同一个文件或对象进行操作，需要添加join()来确保不会死锁。
        也可以通过添加线程锁避免线程死锁。
        锁：当第一条线程运行到文件操作时，加上锁，其余线程就排队等待。
    '''
    # t.join()
