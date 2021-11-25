import pytest

"""
    pytest将在当前目录及其子目录中运行所有格式为test_*.py或者*_test.py文件
"""

def test_01():
    print('test01')
    assert 1==1

if __name__ == '__main__':
    pytest.main(['-s'])