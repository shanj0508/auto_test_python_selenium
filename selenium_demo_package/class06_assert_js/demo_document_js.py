# -*- coding: utf-8 -*-
'''
    Document对象：对于一些特殊场景，可以通过document对象来进行处理
    作用：
        1.定位元素
        2.通过document对象，修改元素属性，添加或移除属性
        3.滚动条操作:目前要么忽略，要么只能通过js来实现
            滚动的比例：
                0-表示最上方
                500-表示中间
                1000-表示末尾
        4.滚动到指定元素:
            操作滚动条的目的就是为了将指定元素显示出来，能够通过selenium进行定位和操作。
'''
from selenium import webdriver
from time import sleep
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.Chrome()
driver.implicitly_wait(10)
sleep(3)
driver.get('http://www.baidu.com')
driver.maximize_window()

driver.find_element('id', 'kw').send_keys(u'自动化测试')
driver.find_element('id', 'su').click()
sleep(2)

# js实现窗口滚动
# # 1.定义js语句
# js = 'window.scrollTo(0,500)'
# # 2.通过js执行器来执行js语句
# driver.execute_script(js)


# 滚动到指定元素
# # 1.找到需要定位的元素
# el = driver.find_element('xpath', '//*[@id="8"]/h3/a')
# # 2.定义js语句
# js = 'arguments[0].scrollIntoView()'
# # 3.调用js执行器,执行js语句，arguments[0]相当于这里传入的el，即需要定位的元素本身。
# driver.execute_script(js, el)
# # arguments相当于占位符，相对document对象，更为灵活。
# # 上面1-3相当于：driver.find_element('xpath', '//*[@id="8"]/h3/a').scrollIntoView()

# 添加元素属性
# # 1.找到需要定位的元素
# el = driver.find_element('id', 'kw')
# # 2.定义js语句
# js = "arguments[0].setAttribute('aaa','bbb')"
# # 3.调用js执行器,执行js语句
# driver.execute_script(js, el)
#
# # 移除元素属性
# # 1.找到需要定位的元素
# el = driver.find_element('id', 'kw')
# # 2.定义js语句
# js = "arguments[0].removeAttribute('name')"
# # 3.调用js执行器,执行js语句
# driver.execute_script(js, el)

# # 通过js获取文本
# # 1.找到需要定位的元素
# el = driver.find_element('xpath', '//*[@id="u"]/a[1]')
# # 2.定义js语句
# js = "arguments[0].innerHTML"
# # 3.调用js执行器,执行js语句
# driver.execute_script(js, el)

# # 给元素设置文本内容
# # 1.找到需要定位的元素
# el = driver.find_element('xpath', '//*[@id="u"]/a[1]')
# # 2.定义js语句
# js = "arguments[0].innerHTML='aaa'"
# # 3.调用js执行器,执行js语句
# driver.execute_script(js, el)

# 通过js获取文本并打印文本内容
# 1.找到需要定位的元素
el = driver.find_element('xpath', '//*[@id="u"]/a[1]')
# 2.定义js语句
js = "return arguments[0].innerHTML"
# 3.调用js执行器,执行js语句
text = driver.execute_script(js, el)
print(text)
js = "return arguments[0].innerHTML='aaa'"
text = driver.execute_script(js, el)
print(text)

# driver.quit()
