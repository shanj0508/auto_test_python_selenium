import pytest

'''
    pytest中用例的管理手段：mark
    可以通过mark装饰器对所有的用例进行标记，不同的标记进行区分进行管理。

'''


# 测试用例
@pytest.mark.webui
def test_01():
    print('web01')


@pytest.mark.webui
@pytest.mark.temp
def test_02():
    print('web02')


@pytest.mark.interface
@pytest.mark.temp
def test_03():
    print('interface01')


@pytest.mark.interface
def test_04(confdemo01):
    print('interface02')
    assert confdemo01 == 2, '失败'


# pytest运行主入口
if __name__ == '__main__':
    pytest.main()
