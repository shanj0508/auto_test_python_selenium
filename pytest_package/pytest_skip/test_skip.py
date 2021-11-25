import pytest

@pytest.mark.skip(reason="no reason")
def test_01():
    print("---用例1执行---")

@pytest.mark.skip
def test_02():
    print("---用例2执行---")

def test_03():
    print("---用例3执行---")

if __name__ == '__main__':
    pytest.main(['-s','test_skip.py'])