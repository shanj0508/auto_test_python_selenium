import pytest

# 功能函数
def multiply(a, b):
    return a * b

"""
    pytest是支持使用测试类的，必须以“Test”开头，注意首字母大写
"""
class TestMultiply:
    # =====fixtures========
    """
        第一批次：setup_ class/ teardown_ class： 在当 前 测试 类 的 开始 与 结束 时 执行。
        第二批次：setup_ method/ teardown_ method： 在 每个 测试 方法 开始 与 结束 时 执行。
        第三批次：setup/ teardown： 在 每个 测试 方法 开始 与 结束 时 执行， 同样 可以 作用于 测试 函数。
         PS：执行顺序按批次顺序来，及时改变方法位置，也是一样
    """
    @classmethod
    def setup_class(cls):
        print("setup_class=========>")

    @classmethod
    def teardown_class(cls):
        print("teardown_class=========>")

    def setup_method(self, method):
        print("setup_method----->>")

    def teardown_method(self, method):
        print("teardown_method-->>")

    def setup(self):
        print("setup----->")

    def teardown(self):
        print("teardown-->")


    # =====测试用例========
    def test_numbers_5_6(self):
        print('test_numbers_5_6')
        assert multiply(5, 6) == 30

    def test_strings_b_2(self):
        print('test_strings_b_2')
        assert multiply('b', 2) == 'bb'

if __name__ == '__main__':
    #“- s” 参数 用于 关闭 捕捉， 从而 输出 打印 信息
    pytest.main(["-s","test_setup02.py"])
