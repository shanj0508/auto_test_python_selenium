import pytest

@pytest.mark.parametrize('a,b',[('zz','123456'),('xz','123456')])
def test_01(a,b):
    print('\n' + a)
    print('\n' + b)

if __name__ == '__main__':
    pytest.main(['-s','teste_multi_parm.py'])