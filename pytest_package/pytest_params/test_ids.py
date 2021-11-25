import pytest

@pytest.mark.parametrize('a,b,c',[(1,1,1),(2,2,0),(3,0,0),(4,4,0)],
                         ids=['用例一','用例二','用例三','用例四'])
def test_1(a,b,c):
    print(a,b,c)

if __name__ == '__main__':
    pytest.main(['-s','-v','test_ids.py'])