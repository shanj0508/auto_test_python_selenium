import pytest

"""
    1)pytest将在当前目录及其子目录中运行所有格式为test_*.py或者*_test.py文件
    2)测试方法/函数默认必须是test开头的
    3)测试类必须是Test
"""
"""
    Python测试发现约定
    *如果未指定任何参数，则收集从testpaths （如果已配置）
    或当前目录开始。另外，命令行参数可以在目录，文件名或节点ID的任何组合中使用。
    *递归到目录，除非它们匹配norecursedirs。
    *在这些目录中，搜索test_*.py或*_test.py。
    *从这些文件中，收集测试项目：
        *在类之外拥有test前缀的测试函数或方法
        *在拥有Test前缀中的测试类（不含__init__方法）中的拥有test前缀的测试函数或方法
    可自定义测试发现规则
    pytest也可以发现使用标准的unittest.TestCase子类技术的测试用例（完全兼容unittest的原因）
"""

def test_01():
    print('test01')
    assert 1==1

if __name__ == '__main__':
    pytest.main(['-s'])
    #命令行参数可以在目录，文件名或节点ID的任何组合中使用。
    # pytest.main(['-s','./testing/test_pytest.py::test_04'])
    # 自定义测试发现规则，比如忽略一些目录
    # pytest.main(['-s','--ignore=testing/','--ignore=doc/'])

