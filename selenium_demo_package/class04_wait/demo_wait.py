# !/usr/bin/env python27
# -*- coding: utf-8 -*-


# 三类等待
'''
    1.等待的作用
        自动化测试首先关注的是成功率，即稳定性。
        自动化测试流程的稳定性需要通过等待来保障。给浏览器以反应的时间。

    2.三类等待
        （1）强制等待：
            不考虑整体代码的连贯性和逻辑性，运行到sleep时，就直接停止指定时间，时间结束后，继续运行后面的代码
            导入：from time import sleep
            语法：sleep(sec)
            优势：容易上手，有需要时直接调用即可。
            劣势：
                -不灵活，哪怕系统提前完成指令的操作，依然要等待到指定时间才会继续下一步。
                -等待时间的设置全凭主观设置，可能不准确。
                -会造成大量的时间浪费，导致执行一个脚本的时间过长。
            一般而言用于调试中。
        （2）隐式等待：
            其本质上是driver的一个设置项，只需要设置一次，即可在整个driver的生命周期中生效。即直到driver.quit()之前，都会有效。
            语法：driver.implicitly_wait(sec)
            执行过程：隐式等待会在指定的时间内一直查找元素，找到元素后立即进入下一步。如果没有找到元素，会一直等待到指定的最大时间，然后执行下一步，报错：找不到元素。

            优势：在整个webdriver的生命周期中，只需要设置一次即可。
            劣势：
                如果找不到元素，就直接进入下一步
                隐式等待必须在页面加载完成之后才生效，即页面在转圈时，隐式等待不生效，即使目标元素已出现，也不会执行下一步。所以隐式等待的执行效率不是太好。
            一般都会添加隐式等待，时间为5s或10s。
        （3）显式等待：
            专门针对元素进行等待的。只需要考虑元素在页面中是否显示，若显示则等待结束。
            和强制等待一样，在需要调用时就定义。
            导入：from selenium.webdriver.support.wait import WebDriverWait
            语法：WebDriverWait(driver,timeout,0.5)  第一个参数是driver,第二个参数是超时时间，第三个参数是查找频率，0.5表示每0.5秒查找元素一次
            显式等待分为 until和 until_not两种函数来实现等待。
            执行过程：如果页面中显示了这个元素，就执行下一步，如果没有找到元素，等到到指定时间后，抛出Timeout异常：selenium.common.exceptions.TimeoutException: Message: 元素查找失败
            显式等待until在执行过程中会有一个return，返回等待元素。
            until_not在执行过程中会返回一个bool值
            优势：可以直接对单个元素进行等待，效率最高
            劣势：代码太长，使用起来比较麻烦，易造成代码冗余
            显式等待还可以作为断言来使用。
        在实际的自动化测试中，三种等待方式是综合运用的。
            创建driver对象时，设置隐式等待。
            当显示等待与隐式等待同时存在时：
                1.如果显式等待的元素找不到，则抛出超时异常。
                2.基于两者等待时间的设定，默认遵循时间更长的等待。

'''
from selenium import webdriver
from time import sleep
import sys

from selenium.webdriver.support.wait import WebDriverWait

reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.Chrome()
# 2.隐式等待
# driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
sleep(3)
driver.maximize_window()
# 1.强制等待
# sleep(2)
driver.find_element('id', 'kw').send_keys(u'自动化测试')
driver.find_element('id', 'su').click()
sleep(2)

# 3.显示等待：until
# 第一种写法：
WebDriverWait(driver, 10, 0.5).until(lambda el: driver.find_element('xpath', '//*[@id="1"]/h3/a'), message='元素查找失败')
driver.find_element('xpath', '//*[@id="1"]/h3/a').click()
# 第二种写法：
el = WebDriverWait(driver, 10, 0.5).until(lambda el: driver.find_element('xpath', '//*[@id="1"]/h3/a'),
                                          message='元素查找失败')
# 3.显示等待：until_not 返回布尔值,因此不支持下面这种写法，会报错：AttributeError: 'bool' object has no attribute 'click'
# el = WebDriverWait(driver, 10, 0.5).until_not(lambda el: driver.find_element('xpath', '//*[@id="1"]/h3/a'),
#                                           message='元素查找失败')
# el.click()
WebDriverWait(driver, 10, 0.5).until_not(lambda el: driver.find_element('xpath', '//*[@id="1"]/h3/a'), message='元素查找失败')
driver.find_element('xpath', '//*[@id="1"]/h3/a').click()

# 报错：selenium.common.exceptions.TimeoutException: Message: 元素查找失败


# driver.quit()

