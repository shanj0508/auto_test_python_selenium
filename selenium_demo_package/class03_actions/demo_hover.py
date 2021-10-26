# -*- coding: utf-8 -*-

'''
    鼠标悬停：通过ActionChains类来实现悬停的操作行为。
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
sleep(3)
driver.maximize_window()
driver.get('http://www.baidu.com')
# 鼠标悬停
el = driver.find_element('xpath', '//span[text()="设置"]')
# 创建一个actions对象，进行悬停的操作
actions = ActionChains(driver)
actions.move_to_element(el).perform()

# 选择下拉选项
driver.find_element('link text', '搜索设置').click()
# 截图
driver.save_screenshot('./img/1.png')

#
'''
    验证码处理：在自动化中非常常见的场景。
    处理方式：
        1.找开发要一个万能验证码
        2.找开发屏蔽验证码
'''
