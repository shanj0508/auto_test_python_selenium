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
    # 将测试发送到多个CPU
    # pytest.main(["-n","2","test_many.py"])
    # 使用与计算机具有CPU内核一样多的进程
    pytest.main(["-n", "auto", "test_many.py"])