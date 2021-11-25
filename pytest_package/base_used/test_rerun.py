import pytest

def test_case01():
    assert 1==1

def test_case02():
    assert 1==1

def test_case03():
    assert 1==3

def test_case04():
    assert 1==4

def test_case05():
    assert 1==5

def test_case06():
    assert 1==1

if __name__ == '__main__':
    # 重新运行所有测试失败，指定测试的最大次数
    # pytest.main(['--reruns','5','test_rerun.py'])
    # 在n次重跑之间，增加一个延迟等待时间
    pytest.main(['--reruns', '3','--reruns-delay','1', 'test_rerun.py'])