# -*- coding: utf-8 -*-
'''
    关键字驱动类
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium_demo_package.homework.my_conf.chrome_options import Options


def open_browser(type_):
    try:
        if type_ == 'Chrome':
            return webdriver.Chrome(options=Options().conf_options())
        else:
            return getattr(webdriver, type_)()
    except:
        return webdriver.Chrome()


class WebKey:
    # 定义常规的测试操作行为

    # 创建构造函数，用于初始化self.driver对象,要考虑到driver对象可能是任意一种浏览器对象
    def __init__(self, text):
        self.driver = open_browser(text)
        # 隐式等待
        self.driver.implicitly_wait(10)

    # 访问url
    def visit(self, text):
        self.driver.get(text)

    # 关闭浏览器driver释放资源
    def quit(self):
        self.driver.quit()

    # 元素定位
    def locator(self, name, value):
        return self.driver.find_element(name, value)

    # 输入
    def input(self, name, value, text):
        self.locator(name, value).send_keys(text)

    # 点击
    def click(self, name, value):
        self.locator(name, value).click()

    # 强制等待
    def sleep(self, text):
        sleep(text)

    # 显示等待
    def wait(self, name, value):
        WebDriverWait(self.driver, 10, 0.1).until(lambda el: self.driver.find_element(name, value),
                                                  message='等待失败')

    # 句柄的切换：包含关闭原页面
    def handle_close(self):
        handles = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(handles[1])

    # 句柄的切换：不包含关闭原页面
    def handle(self, text=1):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[text])

    # 切换frame
    def switch_frame(self, text):
        self.driver.switch_to.frame(text)

    # 获取元素文本
    def get_text(self, name, value):
        return self.locator(name, value).text

    # 获取属性值
    def get_attribute(self, name, value, text):
        return self.locator(name, value).get_attribute(text)

    # 文本断言
    def assert_text(self, name, value, expect):
        try:
            reality = self.locator(name, value).text
            assert reality == expect, '断言失败'
            return True
        except Exception:
            self.log.exception('出现异常，断言失败：{0}!={1}'.format(expect, reality))
            return False

    # 属性断言
    def assert_attr(self, name, value, txt, expect):
        try:
            reality = self.locator(name, value).get_attribute(txt)
            assert reality == expect, '断言失败'
            return True
        except Exception:
            self.log.exception('出现异常，断言失败：{0}!={1}'.format(expect, reality))
            return False

    # 清除文本框内容
    def clear(self, name, value):
        self.locator(name, value).clear()

    # 清除文本框内容并输入新值
    def clear_input(self, name, value, text):
        el = self.locator(name, value)
        el.clear()
        el.send_keys(text)
