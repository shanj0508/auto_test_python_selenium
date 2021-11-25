import pytest

def test_case_01():
    print("我会pytest_config/scripts目录下的用例")
    assert 1==1

if __name__ == '__main__':
    pytest.main()