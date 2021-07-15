# 导入webdriver
from selenium import webdriver
# 导入强制等待
from time import sleep

# 创建一个浏览器对象
driver = webdriver.Chrome()

# 浏览器访问指定的URL
driver.get("https://www.baidu.com/")

# 元素的定位与操作：先获取WebElement对象，然后再考虑元素如何操作
el_input = driver.find_element_by_xpath('//input[@id="kw"]')
el_input.send_keys('python')

el_button = driver.find_element_by_xpath('//input[@id="su"]')
el_button.click()

# WebDriver是服务端代理，当自动化结束的时候，需要释放资源
sleep(5)
driver.quit()
