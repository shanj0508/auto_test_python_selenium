# coding=utf-8
# 导入selenium模块
from selenium import webdriver
# 导入time模块
import time
import unittest


class TestDemo(unittest.TestCase):

    def test_test1(self):
        # 打开Chrome浏览器
        driver = webdriver.Chrome()
        # 打开百度
        driver.get('http://www.baidu.com')
        # 等待3秒
        time.sleep(3)
        # 设置窗口大小为540*960
        driver.set_window_size(540, 960)
        # 浏览器最大化
        driver.maximize_window()
        time.sleep(3)
        # 关闭浏览器窗口
        driver.close()
        # 结束浏览器进程
        driver.quit()

        # # 截屏
        # driver.get_screenshot_as_file('D:\\test\\1.jpg')
        # # 刷新页面
        # driver.refresh()
        # # 返回上一页
        # driver.back()
        # time.sleep(3)
        # # 切换下一页
        # driver.forward()
        # time.sleep(3)
