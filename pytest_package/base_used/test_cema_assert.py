from time import sleep

import pytest
from selenium import webdriver

"""
    Pytest的断言机制，用一句话概括就是借助 Python 的 运算符 号 和 关键字实现断言
"""

# def test_case_01():
    # driver = webdriver.Chrome()
    # driver.get("http://39.98.138.157/shopxo/")
    # driver.find_element_by_link_text("登录").click()
    # sleep(1)
    # driver.find_element_by_xpath("//label[text()='登录账号']/../input").send_keys("zz666")
    # driver.find_element_by_xpath("//label[text()='登录密码']/../input").send_keys("123456")
    # driver.find_element_by_xpath("//button[text()='登录']").click()
    # sleep(3)
    # # 预期结果
    # welcome = driver.find_element_by_xpath("//*[contains(text(),'欢迎来到')]").text
    # assert 'zz666，欢迎来到' == welcome
    # 测试相等 ==
    # 测试不相等 !=
    # <=
    # >=
    # in 测试包含
    # not in 测试不包含
    # 判断是否为true :is True
    # 判断是不不为ture：is not True/is False

    # driver.quit()

def test_kkk_01():
    print("kkk")
    assert 1==2

def test_kkk_02():
    print("kkk")
    assert 1==2

@pytest.mark.slow
def test_kkk_03():
    print("kkk")
    assert 1==1

def test_zzz_04():
    print("zzz")

if __name__ == '__main__':
    # pytest.main(['-s','-v','-k','kkk','test_cema_assert.py'])
    # 最简化信息输出
    # pytest.main(['-q'])
    # 如果一条用例执行失败，立刻退出
    # pytest.main(['-s','-x'])
    # 生成junit xml格式测试报告
    # pytest.main(['-s','--junit-xml=./report/log01.xml'])
    #在第N个用例失败后，结束测试执行
    # pytest.main(['-s', '--maxfail=2'])
    # 执行标记的用例
    # pytest.main(['-s','-m','slow'])
    # 执行未标记的用例
    pytest.main(['-s', '-m', 'not slow'])