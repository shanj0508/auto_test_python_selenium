# -*- coding: utf-8 -*-
'''
    弹窗机制（了解）：现在很少用以下三种弹窗机制了，现在所有的弹窗交互都是基于div直接实现。
    弹窗不是页面弹出的，是浏览器弹出的，遵循浏览器的样式，例如：上传下载文件时的窗口
    在浏览器中有三类弹窗：
        1.alert：仅支持确认
        2.prompt：支持输入并确认
        3.confirm：支持确认与取消

    常用的弹框处理方法：
       alert text                获取警告框的内容
        accept()         相当于点击确认按钮
        dismiss(）     相当于点击取消按钮
        send_keys()  向警告框输入值
'''

from selenium import webdriver

driver = webdriver.Chrome()
# alert弹窗处理
# 跳转到弹窗
# driver.switch_to.alert.accept()
alert = driver.switch_to.alert
# 确认
alert.accept()

# confirm弹窗处理
alert.accept()  # 确定
alert.dismiss()  # 取消

# promt弹窗处理
alert.send_keys()  # 输入
alert.accept()  # 确定
alert.dismiss()  # 取消
