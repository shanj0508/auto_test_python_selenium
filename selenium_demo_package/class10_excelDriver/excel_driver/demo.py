# -*- coding: utf-8 -*-
'''
    反射机制：

'''
from selenium import webdriver

from selenium_demo_package.class10_excelDriver.excel_driver.chrome_options import Options


def open_browser(type_):
    # 基于反射的形态来简化代码
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        # 设置默认driver为chrome浏览器
        driver = webdriver.Chrome(options=Options().conf_options())
    return driver


# 获取属性：在原有类中，获取指定的属性
# getattr()
getattr(webdriver, 'Chrome')
# 上面这句等价于：webdriver.Chrome

getattr(webdriver, 'Chrome')()
# 上面这句等价于：webdriver.Chrome()


# 设置属性：在原有的类中，添加新的属性或修改已有属性的值
# setattr()

# 含有属性；在原有的类中，判断是否存在这个属性
# hasattr()

# 删除属性：在原有的类中，删除已存在的属性
# delattr()
