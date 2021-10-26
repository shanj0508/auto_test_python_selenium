# -*- coding: utf-8 -*-
'''
    ChromeOptions配置:
        作用：专门用于在启动driver对象前，对其进行一系列的配置
        应用：
        1.窗体最大化函数：driver.maximize_window()
            弊端：
                -默认的driver函数运行时会有延时
                -部分页面在driver默认大小启动时会以移动端形式显示页面内容(原因：窗体大小的自适应导致)
            解决方式：通过ChromeOptions配置默认启动的driver窗体最大化
        2.关闭浏览器警告：Chrome正受到自动测试软件的控制
        3.让driver对象加载本地缓存(不推荐，很不友好)
            使用步骤：
                -打开chrom浏览器，访问：chrome://version/,查看【个人资料路径】
                -通过参数--user-data-dir=将个人资料路径加载进driver对象(User Data目录下就是本地的所有缓存数据)
                -在调用本地缓存之前，必须要关闭所有浏览器，否则会报错
            存在的问题：
                在selenium3.x版本，因为要加载本地缓存到浏览器，因此启动浏览器的速度会特别慢，
                需要通过手动输入url进行访问，从而实现加载的提速。很不友好。
                selenium4版本对此进行了优化和提速，启动浏览器速度非常快，可以进行应用。
            应用场景：解决登录和验证码的问题
        4.无头模式：





'''

from selenium import webdriver
from time import sleep

# 配置ChromeOptions
options = webdriver.ChromeOptions()
# 1.默认启动的driver窗体最大化
options.add_argument('start-maximized')
# 2.去掉提示正在执行自动化的警告条
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 老版本去掉警告条方式：现在已经用不了了
# options.add_argument('disable-infobars')
# 3.让driver对象加载本地缓存
options.add_argument(r'--user-data-dir=C:\Users\Shanj\AppData\Local\Google\Chrome\User Data')

# 配置参数加入driver对象
# 老版本
# driver = webdriver.Chrome(chrome_options=options)
# 新版本
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
sleep(3)
# driver.maximize_window()
driver.get('https://www.baidu.com/')
print(driver.title)
