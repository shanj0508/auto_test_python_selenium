'''
这是pytest中的预置函数定义的配置文件

使用@pytest.fixture(scope='module')来定义等级，scope参数有以下4种等级：
    session  :  每个session只运行一次，在自动化测试时，登录步骤可以使用该session
    module   :  每个模块执行(函数形式的用例)
    class    :  每个类执行
    function(默认) :  每一个用例都执行



'''
import pytest


# 定义一个预置函数：用于前期的数据准备
@pytest.fixture()
def confdemo():
    print('这是一个配置demo')
@pytest.fixture()
def confdemo01():
    return 1