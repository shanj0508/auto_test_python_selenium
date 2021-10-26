# coding=utf-8
'''
网易云音乐案例
http://music.163.com
'''
from selenium import webdriver
from time import sleep

# 创建webdriver
driver = webdriver.Chrome()
# 访问url
driver.get('http://music.163.com')
print(driver.window_handles)
# 窗口最大化
driver.maximize_window()
sleep(2)
# 执行登陆流程
driver.find_element('link text', '登录').click()
sleep(2)
driver.find_element('link text', '选择其他登录模式').click()
sleep(2)
# 勾选同意协议复选框
driver.find_element('id', 'j-official-terms').click()
# 选择QQ登陆方式
driver.find_element('link text', 'QQ登录').click()
sleep(2)
'''
句柄的切换:即浏览器打开多个窗口时，窗口之间的切换，如果不切换，则默认只会停留在第一个句柄页
    原则：
        1.在selenium自动化时，尽可能保持有且最多仅有两个页面存在。所以需要在切换句柄操作之前执行driver.close()，关闭当前句柄页。
        2.如果页面会自动关闭，则不需要执行driver.close()
        3.如果关闭页面后仍然需要操作其他页面，则需要切换句柄，否则会报错：该window已被关闭

'''
print(driver.title)
# 1.获取当前所有的句柄
handles = driver.window_handles
print(handles)  # [u'CDwindow-BA4BB2E0-7731-48A1-9F65-EEBB3038F234', u'CDwindow-3AB36DF4-4084-45BF-A395-B133950073A9']
# 关闭当前句柄页
driver.close()
# 2.切换句柄
driver.switch_to.window(handles[1])  # 切换到第二个句柄
print(driver.title)
sleep(2)
# driver.find_element('link text', 'QQ登录').click()

'''
iframe是一个窗体，是html页面中内嵌的html页面，本身是一个独立的html页面
对于iframe内的元素，不能直接定位，需要切换进入iframe页面中，才能进行定位
'''
# iframe的切换1:有id就直接传入id或name
driver.switch_to.frame('ptlogin_iframe')
sleep(2)
# iframe的切换2:没有id，通过元素定位传递id进去
# frame=driver.find_element('id','ptlogin_iframe')
# driver.switch_to.frame(frame)
# 操作iframe内的元素
driver.find_element('link text', '帐号密码登录').click()  # 点击账号密码登陆
sleep(2)

# iframe的切出
driver.switch_to.default_content()  # 返回默认窗体
sleep(2)
driver.find_element('link text', 'QQ登录').click()
sleep(2)
print(driver.title)
handles = driver.window_handles
driver.switch_to.window(handles[1])  # 切换到第二个句柄
sleep(2)
print(driver.title)
