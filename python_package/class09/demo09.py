# 异常处理函数

'''
异常处理函数：
程序在运行时，如果报错，会停止运行并返回错误信息，这就是异常
程序停止并且返回错误信息的过程就叫抛出异常

异常处理有利于程序的稳定性和健壮性，会针对突发的情况做集中处理

语法结构：
try:
    执行的代码
except 已知异常类型:
    出现错误的处理
except Exception as 别名:
    未知异常的处理



程序中，不确定会不会出现问题的代码，就写在try里面，如果程序出现问题，就执行except里面的代码
try except作用就是用来捕获错误信息，捕获到的错误信息会保存在日志里面
'''

# 题目1：要求用户输入整数
# 没有异常处理的情况：
# num = int(input('请输入数字：'))
# print(num)
'''若输入非数字，抛出异常：
请输入数字：你好
Traceback (most recent call last):
  File "D:\github\auto_test_python_selenium\python_package\class09\demo09.py", line 20, in <module>
    num = int(input('请输入数字：'))
ValueError: invalid literal for int() with base 10: '你好'
'''
# 异常处理的情况：
# try:
#     num = int(input('请输入数字：'))
#     print(num)
# except:
#     print('请输入正确的数字')

'''捕获异常：
请输入数字：你好
请输入正确的数字

Process finished with exit code 0
'''

# 题目2：用户输入一个数字，进行2整除
# 没有异常处理的情况：
# num = int(input('请输入数字：'))
# result = 2 / num
# print(result)
'''若输入非数字，抛出异常：
请输入数字：你好
Traceback (most recent call last):
  File "D:\github\auto_test_python_selenium\python_package\class09\demo09.py", line 46, in <module>
    num = int(input('请输入数字：'))
ValueError: invalid literal for int() with base 10: '你好'
'''
# ValueError是这个错误的类型
'''若输入0，除数不能为0，抛出异常：
请输入数字：0
Traceback (most recent call last):
  File "D:\github\auto_test_python_selenium\python_package\class09\demo09.py", line 47, in <module>
    result = 2 / num
ZeroDivisionError: division by zero
'''
# ZeroDivisionError是这个错误的类型

# 异常处理的情况：
# try:
#     num = int(input('请输入数字：'))
#     result = 2 / num
#     print(result)
# except ZeroDivisionError:
#     print('除数不能为0')
# except ValueError:
#     print('请输入正确的数字')
'''捕获异常：
请输入数字：0
除数不能为0

请输入数字：你好
请输入正确的数字
'''

'''
常见的异常类型：
ZeroDivisionError: 除法运算中除数为 0 引发此异常
NameError: 尝试访问一个未声明的变量时，引发此异常
TypeError: 不同类型数据之间的无效操作
IndexError：索引超出序列范围会引发此异常
AssertionError： 当 assert 关键字后的条件为假时，程序运行会停止并抛出 AssertionError 异常
KeyError： 字典中查找一个不存在的关键字时引发此异常

'''

# 未知异常的处理
# try:
#     num = int(input('请输入数字：'))
#     result = 2 / num
#     print(result)
# except ZeroDivisionError:
#     # 已知异常
#     print('除数不能为0')
# except Exception as e:
#     print('未知的错误打印：%s' % e)  # 未知的错误打印：invalid literal for int() with base 10: '你好'

# 异常的传递：我们可以在函数定义时进行异常的捕获和处理，也可以在函数调用时进行异常的捕获和处理
# 一个函数里面只能有一个try
# 函数定义时异常处理：
# def demo1():
#     try:
#         num = int(input('请输入数字：'))
#         return num
#     except Exception as e:
#         print('未知错误：%s' % e)
#
# res = demo1()
# print(res)
'''
请输入数字：你好
未知错误：invalid literal for int() with base 10: '你好'
None
'''
# 函数调用时异常处理：
# def demo2():
#     num = int(input('请输入数字：'))
#     return num
#
# try:
#     res = demo2()
#     print(res)
# except Exception as e:
#     print('未知错误：%s'%e)

'''
请输入数字：你好
未知错误：invalid literal for int() with base 10: '你好'
'''

'''
完整的语法结构：

try:
    执行的代码
except 已知异常类型:
    出现错误的处理
except Exception as 别名:
    未知异常的处理
else:
    没有异常的代码会执行这里
finally:
    无论程序有没有异常，都会被执行的代码
'''
# try:
#     num = int(input('请输入数字：'))
#     result = 2 / num
#     print(result)
# except ZeroDivisionError:
#     # 已知异常
#     print('除数不能为0')
# except Exception as e:
#     # 未知异常
#     print('未知的错误捕获：%s' % e)  # 未知的错误打印：invalid literal for int() with base 10: '你好'
# else:
#     print('没有异常的代码会执行')
# finally:
#     print('无论有没有异常，都会被执行')

'''
请输入数字：0
除数不能为0
无论有没有异常，都会被执行

请输入数字：你好
未知的错误捕获：invalid literal for int() with base 10: '你好'
无论有没有异常，都会被执行

请输入数字：1
2.0
没有异常的代码会执行
无论有没有异常，都会被执行
'''

'''
语法结构：raise异常：主动抛出异常，用于特定的需求

'''


# 需求:定义一个函数，函数提示输入用户密码
# 如果密码长度小于8，抛出异常
# 如果密码长度大于或等于8，返回输入的密码

def input_pwd():
    # 用户输入密码
    pwd = input('请输入密码：')
    # 如果密码长度大于或等于8，返回输入的密码
    if len(pwd) >= 8:
        return pwd
    # 如果密码长度小于8，抛出异常，提示：密码长度不够8位
    exc = Exception('密码长度不够8位')
    raise exc


# u_pwd = input_pwd()
# print(u_pwd)


'''主动抛出异常：
请输入密码：1234567
Traceback (most recent call last):
  File "D:\github\auto_test_python_selenium\python_package\class09\demo09.py", line 206, in <module>
    u_pwd = input_pwd()
  File "D:\github\auto_test_python_selenium\python_package\class09\demo09.py", line 203, in input_pwd
    raise exc
Exception: 密码长度不够8位

Process finished with exit code 1

'''

# 捕获异常
try:
    u_pwd = input_pwd()
    print(u_pwd)
except Exception as e:
    print('捕获未知异常：%s' % e)

'''捕获未知异常：
请输入密码：1234567
捕获未知异常：密码长度不够8位
'''
