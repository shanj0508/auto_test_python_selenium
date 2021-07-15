# 导入webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# 创建一个浏览器对象
wb = WebDriver(executable_path="chromedriver")

# 浏览器访问指定的URL
wb.execute('get', {'url': 'https://www.baidu.com/'})

# 元素的定位与操作：先获取WebElement对象，然后再考虑元素如何操作
el = wb.execute('findElement', {
    'using': By.XPATH,
    'value': '//input[@id="kw"]'

})['value']
print(type(el))
print(el)

el._execute("sendKeysToElement",
            {'text': 'python',
             'value': ''})

el2 = wb.execute('findElement', {
    'using': By.XPATH,
    'value': '//input[@id="su"]'

})['value']

el2._execute("clickElement")
