import pytest

'''
    pytest默认寻找当前路径下所有的文件与子文件夹中以为test开头的文件夹、文件、函数作为识别对象;
    pytest默认不输出任何打印信息，如果要看打印信息，需要在运行时添加-s指令;
    多条指令一同运行时，需要通过空格进行区分，在main函数中，是通过,进行分隔;
    -v 用于详细显示日志信息
    -rA short test summary info 测试结果的简单的统计
    pytest中的setup和teardown：一般可以通过一个配置文件进行直接进行管理，配置文件名一定要是conftest.py
'''


# 前置后置
def setup_function():
    print('setup_function')


def teardown_function():
    print('teardown_function')


def setup_module():
    print('setup_module')


def teardown_module():
    print('teardown_module')


# 测试用例

def test_02():
    print('test102')


def test_01():
    print('test101')


# pytest中class对象的定义：建议以Test开头
class Demo:
    # class内部的前置后置-function级别
    def setup(self):
        print('class内部的setup')

    def teardown(self):
        print('class内部的teardown')

    # class内部的前置后置-class级别
    def setup_class(self):
        print('class内部的setup_class')

    def teardown_class(self):
        print('class内部的teardown_class')

    # class内部的前置后置-method级别
    def setup_method(self):
        print('class内部的setup_method')

    def teardown_method(self):
        print('class内部的teardown_method')

    def test_d1(self):
        print('test_d1')

    def test_d2(self):
        print('test_d2')


# pytest运行主入口
if __name__ == '__main__':
    pytest.main(['-s', '-v', '-rA', 'test_case01.py'])
