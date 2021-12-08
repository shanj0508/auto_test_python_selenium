# -*- coding: utf-8 -*-

'''
    demo:给定一个不超过5位数的正整数，判断其有几位
'''


# 实现一：将数字转为字符串类型，判断字符串的len()
def judgment_digit1():
    input_num = str(input('请输入一个5位的正整数：'))
    digit = len(input_num)
    print('输入的数字是：{},这是一个{}位数'.format(input_num, digit))
    if digit == 1:
        print 1
    elif digit == 2:
        print 2
    elif digit == 3:
        print 3
    elif digit == 4:
        print 4
    else:
        print 5


# judgment_digit1()

# 实现二：判断数字范围
def judgment_digit2():
    input_num = input('请输入一个5位的正整数：')
    print(input_num)
    print(type(input_num))
    print('输入的数字是：{}'.format(input_num))
    if input_num < 10:
        print 1
    elif input_num < 100:
        print 2
    elif input_num < 1000:
        print 3
    elif input_num < 10000:
        print 4
    else:
        print 5


# judgment_digit2()

# 实现三：整除
# 不推荐：因为引入了多次不该用的计算
# 原则：能比较就不计算
def judgment_digit3():
    input_num = input('请输入一个5位的正整数：')
    print(input_num)
    print(type(input_num))
    print('输入的数字是：{}'.format(input_num))
    if input_num // 10000:
        print 5
    elif input_num // 1000:
        print 4
    elif input_num // 100:
        print 3
    elif input_num // 10:
        print 2
    else:
        print 1


# judgment_digit3()
# 实现四：采用了折半的思想,代码效率比较高
def judgment_digit4():
    input_num = input('请输入一个5位的正整数：')
    print(input_num)
    print(type(input_num))
    print('输入的数字是：{}'.format(input_num))
    if input_num >= 100:
        if input_num >= 10000:
            print 5
        elif input_num >= 1000:
            print 4
        else:
            print 3
    else:
        if input_num >= 10:
            print 2
        else:
            print 1


judgment_digit4()
