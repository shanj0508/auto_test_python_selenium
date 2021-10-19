# 常规元素操作行为：
from selenium import webdriver
from time import sleep

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

# 窗体最大化:有些元素必须在窗体最大化的情况下才可以执行操作
# 元素无法正常交互的异常：
#   1.一般是因为当前展示的页面内容无法查找到这个元素，所以抛出异常。
#   2.元素定位错误，定位到其他同名元素，且这个元素在页面中不显示。
driver.maximize_window()

# 访问URL
driver.get('http://39.98.138.157/shopxo/index.php')
sleep(3)
# 点击：任何元素都可以调用click
driver.find_element('xpath', '//div[@class="menu-hd"]/a[text()="登录"]').click()
sleep(3)
# 输入：只有input标签和textarea标签支持sendkeys输入
driver.find_element('name', 'accounts').send_keys('shanjing')
sleep(1)
driver.find_element('name', 'pwd').send_keys('shanjing@.000')
sleep(3)
driver.find_element('xpath', '//button[text()="登录"]').click()
# 注意：input标签的文件上传可以使用sendkeys,非input标签的文件上传需要使用autoIT

# 文件上传demo
# driver.get('https://image.baidu.com/')
# sleep(3)
# driver.find_element('xpath','//*[@id="sttb"]/img[1]').click()
# sleep(3)
# driver.find_element('id','stfile').send_keys(r'D:\github\auto_test_python_selenium\selenium_demo_package\class03_actions\3.jpeg')

# 下拉列表框
# 1.定位select元素
el = driver.find_element('name', 'schoolid')
# 2.转成select对象
select = Select(el)

# 3.1获取所有的option内容,通过for循环遍历所有的li
li = select.options
# 3.2获取指定的值，进行传入
select.select_by_value('2913')  # value
select.select_by_index(0)  # 下标，不推荐
select.select_by_visible_text('北京八中固安分校')  # 文本

# 释放资源
driver.quit()
