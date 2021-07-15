# coding=utf-8
from selenium import webdriver
import time
import unittest


class TestPathDemo(unittest.TestCase):
    def test_serchBaidu01_by_id(self):
        # 启动浏览器
        driver = webdriver.Chrome()
        # 打开百度首页
        driver.get('http://www.baidu.com')
        # 浏览器最大化
        driver.maximize_window()
        # 等待2秒
        time.sleep(2)
        # 通过id=kw定位搜索框，并输入selenium
        driver.find_element_by_id('kw').send_keys('selenium')
        # 通过id定位'百度一下'按钮,并点击
        time.sleep(2)
        btn = driver.find_element_by_id('su')
        btn.click()
        # 等待5秒
        time.sleep(5)
        # 退出
        driver.quit()

    def test_serchBaidu02_by_name(self):
        # 启动浏览器
        driver = webdriver.Chrome()
        # 打开百度首页
        driver.get('http://www.baidu.com')
        # 浏览器最大化
        driver.maximize_window()
        # 等待2秒
        time.sleep(2)
        # 通过name=wd定位搜索框，并输入selenium
        driver.find_element_by_name('wd').send_keys('selenium')
        # 等待5秒
        time.sleep(5)
        # 退出
        driver.quit()

    def test_serchBaidu03_by_class_name(self):
        # 启动浏览器
        driver = webdriver.Chrome()
        # 打开百度首页
        driver.get('http://www.baidu.com')
        # 浏览器最大化
        driver.maximize_window()
        # 等待2秒
        time.sleep(2)
        # 通过class=s_ipt定位搜索框，并输入selenium
        driver.find_element_by_class_name('s_ipt').send_keys('selenium')
        # 通过class_name定位'百度一下'按钮,并点击
        time.sleep(2)
        btn = driver.find_element_by_class_name('s_btn')
        btn.click()
        # 等待5秒
        time.sleep(5)
        # 退出
        driver.quit()

    def test_serchBaidu04_by_tag_name(self):
        # 启动浏览器
        driver = webdriver.Chrome()
        # 打开百度首页
        driver.get('http://www.baidu.com')
        # 浏览器最大化
        driver.maximize_window()
        # 等待2秒
        time.sleep(2)
        # 通过tag=input定位搜索框，并输入selenium
        driver.find_element_by_tag_name('input').send_keys('selenium')
        # 等待5秒
        time.sleep(5)
        # 退出
        driver.quit()

    def test_serchBaidu05_by_link_text(self):
        # 启动浏览器
        driver = webdriver.Chrome()
        # 打开百度首页
        driver.get('http://www.baidu.com')
        # 浏览器最大化
        driver.maximize_window()
        # 等待2秒
        time.sleep(2)
        # 通过link_text='新闻'定位超链接，并点击
        driver.find_element_by_link_text('新闻').click()
        # 等待5秒
        time.sleep(5)
        # 退出
        driver.quit()

    def test_serchBaidu06_by_partial_link_text(self):
        # 启动浏览器
        driver = webdriver.Chrome()
        # 打开百度首页
        driver.get('http://www.baidu.com')
        # 浏览器最大化
        driver.maximize_window()
        # 等待2秒
        time.sleep(2)
        # 通过partial_link='闻'定位'新闻'超链接，并点击
        driver.find_element_by_partial_link_text('闻').click()
        # 等待5秒
        time.sleep(5)
        # 退出
        driver.quit()

    def test_serchBaidu07_by_xpath(self):
        # 启动浏览器
        driver = webdriver.Chrome()
        # 打开百度首页
        driver.get('http://www.baidu.com')
        # 浏览器最大化
        driver.maximize_window()
        # 等待2秒
        time.sleep(2)
        # 通过xpath定位搜索框，并输入selenium
        driver.find_element_by_xpath("//*[@id='kw']").send_keys('selenium')
        # 等待5秒
        time.sleep(5)
        # 退出
        driver.quit()

    def test_serchBaidu08_by_css_selector(self):
        # 启动浏览器
        driver = webdriver.Chrome()
        # 打开百度首页
        driver.get('http://www.baidu.com')
        # 浏览器最大化
        driver.maximize_window()
        # 等待2秒
        time.sleep(2)
        # 通过CSS定位搜索框，并输入selenium
        driver.find_element_by_css_selector('#kw').send_keys('selenium')
        # 等待5秒
        time.sleep(5)
        # 退出
        driver.quit()
