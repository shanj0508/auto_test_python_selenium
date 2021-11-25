import pytest

def test_case_01():
    print("我会pytest_config/scripts目录下auto*文件的用例")
    assert 1==1

class Auto_case():
    def test_class_case01(self):
        print("我是类Auto_case中的用例test_class_case01")

    def auto_case01(self):
        print("我是类Auto_case中的用例auto_case01")

class B_case():
    def test_class_case01(self):
        print("我是类B中的用例test_class_case01")

if __name__ == '__main__':
    pytest.main()