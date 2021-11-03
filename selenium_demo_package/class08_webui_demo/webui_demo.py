# -*- coding: utf-8 -*-
'''
    1.实现登录流程
    2.添加商品（手机）流程
'''

from selenium import webdriver
from time import sleep
# import sys

from selenium.webdriver.support.wait import WebDriverWait

from selenium_demo_package.class08_webui_demo.chrome_options import Options

# reload(sys)
# sys.setdefaultencoding('utf-8')

num = '4'

driver = webdriver.Chrome(options=Options().conf_options())
driver.implicitly_wait(10)
driver.get('http://39.98.138.157/shopxo/')
# 1.登录操作
driver.find_element('link text', '登录').click()
el = WebDriverWait(driver, 5, 0.1).until(lambda el: driver.find_element('xpath', '//*[text()="还没有帐号？"]'),
                                         message='登陆页面跳转失败')
print('跳转登陆页面成功')
driver.find_element('name', 'accounts').send_keys('shanjing')
driver.find_element('name', 'pwd').send_keys('shanjing@.000')
driver.find_element('xpath', '//button[text()="登录"]').click()
el = WebDriverWait(driver, 5, 0.1).until(lambda el: driver.find_element('xpath', '//*[text()="登录成功"]'),
                                         message='登录失败')
print('登录成功')
# 断言
# 获取退出按钮的文本
text = driver.find_element('link text', '退出').text
print(text)
# 校验文本是否符合预期结果
assert text == '退出', '断言失败'

# 2.添加商品：手机
driver.find_element('id', 'search-input').send_keys(u"手机")
driver.find_element('id', 'ai-topsearch').click()
el = WebDriverWait(driver, 5, 0.1).until(
    lambda el: driver.find_element('xpath', '//*[text()="苹果（Apple）iPhone 6 Plus (A1524)移动联通电信4G手机 金色 16G"]'),
    message='搜索失败')
print('搜索成功')
driver.find_element('xpath', '//div[@class="items"]/a[1]').click()
# 句柄切换
handles = driver.window_handles
driver.close()
driver.switch_to.window(handles[1])

# 添加商品属性
driver.find_element('xpath', '//li[@data-value="套餐一"]').click()
sleep(1)
driver.find_element('xpath', '//li[@data-value="金色"]').click()
sleep(1)
driver.find_element('xpath', '//li[@data-value="128G"]').click()
el = driver.find_element('id', 'text_box')
el.clear()
el.send_keys(num)
driver.find_element('xpath', '//button[@title="加入购物车"]').click()
el = WebDriverWait(driver, 5, 0.1).until(
    lambda el: driver.find_element('xpath', '//*[text()="加入成功"]'),
    message='商品添加购物车失败')
print('商品添加购物车成功')

# 进入购物车页面，检查商品是否添加成功：1.商品是否存在购物车；2.商品数量是否与添加的相符

driver.find_element('xpath', '//span[text()="购物车"]').click()
# 检查购物车存在商品

el = WebDriverWait(driver, 5, 0.1).until(
    lambda el: driver.find_element('xpath', '//div[@class="goods-base"]'),
    message='购物车没有该商品')
print('购物车商品存在')

# 检查商品数量
value = driver.find_element('xpath', '//input[@type="number"]').get_attribute("value")
print(value)
assert value == num, '商品数量不正确'

# driver.quit()
