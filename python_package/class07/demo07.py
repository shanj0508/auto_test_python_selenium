# 文件处理与os模块
'''
文件的基本操作：
    1.打开文件:open(文件路径，访问模式)
        主模式：r-只读 w-只写 a-只写
        其他模式：
            r+:在r的基础上增加了可写功能
            w+:在w的基础上增加了可读功能
            a+:在w的基础上增加了可读功能


    2.写入文件:文件对象.write('文件内容')
    3.关闭文件：文件对象.close()  避免占用服务器资源
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
# seek表示偏移量，即指针位置，0表示从头开始，1表示当前位置，2表示文件结尾

f = open('test3.txt', 'w+')
print(f.tell())  # 0
f.write('ddddd')
print(f.tell())  # 5
f.seek(0)  # 设置偏移量从文件末尾到开头，这样可以从0开始读取文件内容
content = f.read()
print(content)
f.close()

# a+:可写可读
