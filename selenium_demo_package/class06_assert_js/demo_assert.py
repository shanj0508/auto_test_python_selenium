# -*- coding: utf-8 -*-
from selenium import webdriver
import sys
from selenium.webdriver.support.wait import WebDriverWait

reload(sys)
sys.setdefaultencoding('utf8')

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
driver.find_element('name', 'accounts').send_keys('shanjing')
driver.find_element('name', 'pwd').send_keys('shanjing@.000')
driver.find_element('xpath', '//button[text()="登录"]').click()
# 显式等待断言
el = WebDriverWait(driver, 5, 0.1).until(lambda el: driver.find_element('xpath', '//*[text()="登录成功"]'),
                                         message='登录失败')
print('登录成功')
# assert断言
# 获取退出按钮的文本
text = driver.find_element('link text', '退出').text
print(text)
# 校验文本是否符合预期结果
assert text == '退出', '断言失败'
