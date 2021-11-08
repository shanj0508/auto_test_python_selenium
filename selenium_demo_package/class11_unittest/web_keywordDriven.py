# -*- coding: utf-8 -*-
'''
    关键字驱动类：
        将selenium中我们需要的内容进行提取和封装，变成适用于我们自己实际应用的内容。
        关键字驱动相当于selenium的二次封装。
    常用的selenium操作行为：
        元素定位
        输入
        点击
        关闭
        等待
        切换句柄
        访问url
        创建webdriver对象
        ……
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium_demo_package.class11_unittest.chrome_options import Options


# 在后续的自动化中，通过调用这个类进行自动化操作，逻辑代码

# 要满足创建任意一个浏览器对象的需求

def open_browser(type_):
    # 基于反射的形态来简化代码
    # try:
    #     driver = getattr(webdriver, type_)()
    # except Exception as e:
    #     print(e)
    #     # 设置默认driver为chrome浏览器
    #     driver = webdriver.Chrome(chrome_options=Options().conf_options())
    # return driver

    # 也可以写成以下形式:
    try:
        if type_ == 'Chrome':
            return webdriver.Chrome(options=Options().conf_options())
        else:
            return getattr(webdriver, type_)()
    except:
        return webdriver.Chrome()


class WebKey:
    # 定义常规的测试操作行为
    # 创建一个临时的driver对象，便于代码的编写。
    # driver = webdriver.Chrome()

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

    # 元素定位:目的是为了通过定义一个方法来实现所有的元素定位。
    # 因为元素定位后，我们会在后续对这个元素进行一系列的操作，所以必须将定位的元素对象return回来，否则后续操作点击、输入等操作时会报错
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

    # 隐式等待：不需要封装，因为它是配置固定的等待时间

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
    # def get_text(self, name, value):
    #     return self.locator(name, value).text

    # 文本断言
    def assert_text(self, name, value, text):
        try:
            assert self.locator(name, value).text == text, '断言失败'
            return True
        except:
            return False

    # 清除文本框内容
    def clear(self, name, value):
        self.locator(name, value).clear()

    # 清除文本框内容并输入新值
    def clear_input(self, name, value, text):
        el = self.locator(name, value)
        el.clear()
        el.send_keys(text)

    # 获取属性值
    def get_attribute(self, name, value, text):
        return self.locator(name, value).get_attribute(text)
