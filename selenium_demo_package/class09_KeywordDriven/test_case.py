# -*- coding: utf-8 -*-
'''
    基于关键字驱动实现的测试用例
'''


# 测试用例1:实现电商的登录
from selenium_demo_package.class09_KeywordDriven.web_keywordDriven import WebKey

num = '4'

# wk = WebKey('Chrome')
# wk.visit('http://39.98.138.157/shopxo/')
# wk.click('link text', '登录')
# wk.wait('xpath', '//*[text()="还没有帐号？"]')
# wk.input('name', 'accounts', 'shanjing')
# wk.input('name', 'pwd', 'shanjing@.000')
# wk.click('xpath', '//button[text()="登录"]')
# wk.wait('xpath', '//*[text()="登录成功"]')
# # 断言
# # 获取退出按钮的文本
# text = wk.get_text('link text', '退出')
# print(text)
# # 校验文本是否符合预期结果
# assert text == '退出', '断言失败'
#
# # 添加商品：手机
# wk.input('id', 'search-input', u"手机")
# wk.click('id', 'ai-topsearch')
# wk.wait('xpath', '//*[text()="苹果（Apple）iPhone 6 Plus (A1524)移动联通电信4G手机 金色 16G"]')
# wk.click('xpath', '//div[@class="items"]/a[1]')
# wk.handle_close()
# # 添加商品属性
# wk.click('xpath', '//li[@data-value="套餐一"]')
# wk.sleep(1)
# wk.click('xpath', '//li[@data-value="金色"]')
# wk.sleep(1)
# wk.click('xpath', '//li[@data-value="128G"]')
# # wk.clear('id', 'text_box')
# # wk.input('id', 'text_box', num)
# wk.clear_input('id', 'text_box', num)
# wk.click('xpath', '//button[@title="加入购物车"]')
# wk.wait('xpath', '//*[text()="加入成功"]')
# # 进入购物车页面，检查商品是否添加成功：1.商品是否存在购物车；2.商品数量是否与添加的相符
# wk.click('xpath', '//span[text()="购物车"]')
# # 检查购物车存在商品
# wk.wait('xpath', '//div[@class="goods-base"]')
#
# # 检查商品数量
# value = wk.get_attribute('xpath', '//input[@type="number"]', "value")
# assert value == num, '商品数量不正确'
# wk.quit()

# 测试用例2：百度搜索

wk = WebKey('Chrome')
wk.visit('http://www.baidu.com')
wk.input('id', 'kw', 'test')
wk.click('id', 'su')
wk.wait('xpath', '//*[@id="1"]')
wk.quit()