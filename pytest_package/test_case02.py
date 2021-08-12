import pytest

# 测试用例

def test_02():
    print('test202')


def test_01():
    print('test201')


# pytest运行主入口
if __name__ == '__main__':
    pytest.main(['-s'])
