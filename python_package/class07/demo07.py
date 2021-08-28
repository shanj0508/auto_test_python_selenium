# 文件处理与os模块
'''
文件的基本操作：
    1.打开文件:open(文件路径，访问模式)
        主模式：r-只读 w-只写 a-只写
        其他模式：
            r+:在r的基础上增加了可写功能
            w+:在w的基础上增加了可读功能
            a+:在w的基础上增加了可读功能
            rb,wb用于二进制文件

    2.读取文件：文件对象.read()   （通过print打印）
    3.写入文件: 文件对象.write('文件内容')
    4.关闭文件：文件对象.close()  避免占用服务器资源
'''
# 初体验
# # 1.打开文件
# f = open('test.txt', 'w')
# # 2.写入文件
# f.write('''aaa
# bbb
# ccc
# ''')
# # 3.关闭文件
# f.close()

# 1.打开文件:open(文件路径，访问模式)

# r-只读模式
# 打开并读取不存在的文件,报错：FileNotFoundError: [Errno 2] No such file or directory: 'test1.txt'
# f = open('test1.txt', 'r')
# content = f.read()
# print(content)
# f.close()
# 打开并读取存在的文件
# f = open('test.txt', 'r')
# content = f.read()
# print(content)
# f.close()

# 只读模式进行写文件,报错：io.UnsupportedOperation: not writable
# f = open('test.txt', 'r')
# content = f.read()
# print(content)
# f.write('写入只读文件')
# f.close()

# w - 只写
# 打开不存在的文件进行写入
# 如果文件不存在，会新建文件再进行写入,写入的内容会覆盖原有的文件内容
# f = open('test1.txt', 'w')
# f.write('123')
# f.close()

# a-只写
# 打开不存在的文件进行写入
# 如果文件不存在，会新建文件再进行写入,写入的内容不会覆盖原有的文件内容,会在原有文件内容后面追加新写入的文件内容
# f = open('test2.txt', 'a')
# f.write('789')
# f.close()


# r+:可读可写
# 打开并读取不存在的文件,报错：FileNotFoundError: [Errno 2] No such file or directory: 'test3.txt'
# 如果文件不存在，会报错,如果文件存在，新写入的内容会覆盖原有的文件内容，r+的文件指针在开头
# f = open('test2.txt', 'r+')
# # 获取文件指针位置  tell
# # open文件后，默认指针位置在0的位置 当前文件内容是：12345
# print(f.tell())  # 0
# # write时，从指针位置开始向后覆盖文件内容
# f.write('aa')  # aa345
# f.close()

# open和read后，文件指针位置发生变化
# f = open('test2.txt', 'r+')
# # 获取文件指针位置  tell
# # open文件后，默认指针位置在0的位置
# print(f.tell())  # 0
# content = f.read()
# print(content)  # 123000
# # read文件后，指针位置在当前文件最后一个字符后面
# print(f.tell())  # 6
# f.write('aa')  # 123000aa
# f.close()


# w+:可写可读
# 打开并读取不存在的文件,如果文件不存在，不会报错,会新建文件。
# 如果文件存在，则原有内容会被删除，新写入的内容会覆盖原有的文件内容，w+的文件指针在开头
# f = open('test3.txt', 'w+')
# f.write('dd')
# f.close()

# f = open('test3.txt', 'w+')
# content = f.read()
# print(content)  # 这里不会打印内容，因为read时原有内容已被删除，无法读取文件内容
# f.close()

# f = open('test3.txt', 'w+')
# content = f.read()
# print(f.tell())  # 0
# f.write('dd')
# print(f.tell())  # 2
# f.close()

# 如果非要读取文件内容，用seek
# seek(偏移量，指针位置) 0表示从头开始，1表示当前位置，2表示文件结尾

# f = open('test3.txt', 'w+')
# print(f.tell())  # 0
# f.write('abcde')
# print(f.tell())  # 5
# f.seek(0)  # 设置偏移量从文件末尾到开头，这样可以从0开始读取文件内容
# content = f.read()
# print(content)  # abcde
# f.close()
#
# f = open('test3.txt', 'w+')
# print(f.tell())  # 0
# f.write('abcde')
# print(f.tell())  # 5
# f.seek(2, 0)  # 设置偏移量从第二个元素开始
# content = f.read()
# print(content)  # cde
# f.close()


# a+:可写可读
# 打开并读取不存在的文件,如果文件不存在，不会报错,会新建文件。
# 如果文件存在，则会在原有内容后面追加新写入的内容，a+的文件指针在文件内容末尾
# f = open('test4.txt', 'a+')
# print(f.tell())  # 0
# f.write('qwe')
# print(f.tell())  # 3
# content = f.read()
# print(content)  #为空，因为文件指针在末尾，所以读不到数据
# f.close()

# 路径
# # 1.同级目录
# # 直接读文件名
# f = open('test4.txt', 'r')
# content = f.read()
# print(content)
# f.close()
# # 读取./文件名
# f = open('./test4.txt', 'r')
# content = f.read()
# print(content)
# f.close()
#
# # 2.父层级目录
# f = open('../__init__.py', 'r')
# content = f.read()
# print(content)
# f.close()


# with..open()as可以不用关闭文件
'''
with open(文件路径，模式)as 别名：
    文件操作
'''
# with open('test5.txt', 'r')as f:
#     print(f.read())


# 2.读取文件：read()   readline()  readlines()
# read()：不传参，默认读取全部文件内
# f = open('test5.txt', 'r')
# content = f.read()
# print(content)  # abcdefg
# f.close()

# read(字符数)
# f = open('test5.txt', 'r')
# content = f.read(2)  # 读取两个字符
# print(content)  # ab
# f.close()

# readline():只读取一行数据
# f = open('test5.txt', 'r')
# content = f.readline()
# print(content)  # abcdefg0
# f.close()

# readlines():默认读取全部数据，以列表形式返回
# f = open('test5.txt', 'r')
# content = f.readlines()
# print(content)  # ['abcdefg0\n', 'abcdefg1\n', 'abcdefg2']
# f.close()

# readlines()[元素下标]:指定读取某一行元素
# f = open('test5.txt', 'r')
# content = f.readlines()[1]
# print(content)  # abcdefg1
# f.close()

# readlines()一般与for循环结合使用
# f = open('test5.txt', 'r')
# for i in f.readlines():
#     print(i)
# f.close()
# 执行结果
# abcdefg0
#
# abcdefg1
#
# abcdefg2


# 3.写入文件: 文件对象.write('文件内容')
# f = open('test6.txt', 'w')
# f.write('dd')
# f.close()
# 4.关闭文件：文件对象.close()  避免占用服务器资源

# os模块：用来处理文件或文件目录
# 1. 直接导入
import os
import shutil

# 路径转义：r 或 \\
file1 = r'D:\github\auto_test_python_selenium\python_package\class07\a'
# 创建一个文件目录
# os.mkdir(file1)

# 删除文件目录
# os.rmdir(file1)

# 若文件目录不是空的，则无法通过rmdir删除，可以通过：shutil.rmtree删除整个文件目录及目录下的文件
# shutil.rmtree(file1)

# 重命名
# os.rename(file1,r'D:\github\auto_test_python_selenium\python_package\class07\b')

# 获得当前文件目录的路径 os.getcwd()
# print(os.getcwd())  # D:\github\auto_test_python_selenium\python_package\class07

# 获得当前文件路径 os.path.join()
# print(os.path.join(os.getcwd(), 'demo07.py'))  # D:\github\auto_test_python_selenium\python_package\class07\demo07.py

# 获取文件权限  os.access(path,mode)
# F_OK(是否存在), R_OK(可读),W_OK可写),X_OK(可执行)
file2 = r'D:\github\auto_test_python_selenium\python_package\class07\demo07.py'
print(os.access(file2, os.F_OK))  # True
print(os.access(file2, os.R_OK))  # True
print(os.access(file2, os.W_OK))  # True
print(os.access(file2, os.X_OK))  # True

# os.chmod
