# -*- coding: utf-8 -*-
'''
    demo:输入两个数字，输出最大数
    注意：比较大小需要数据类型相同
'''


# num = input(">>>")
# print(id(num))
# num = str(num)
# print(id(num))
# num = int(num)
# print(num)
# print(type(num))
# print(id(num))


def output_max_of_two():
    first_num = input('请输入第一个数字：')
    second_num = input('请输入第二个数字：')
    print('第一个数字是：{},第二个数字是：{}'.format(first_num, second_num))
    print('第一个数字是：%d,第二个数字是：%s' % (first_num, second_num))
    print(type(first_num))  # <type 'int'>
    print(type(second_num))  # <type 'int'>
    # if first_num >= second_num:
    #     print('两个数中的最大值是：{}'.format(first_num))
    # else:
    #     print('两个数中的最大值是：{}'.format(second_num))

    # max()
    # print('两个数中的最大值是：{}'.format(max(first_num, second_num)))


# output_max_of_two()
'''
    demo:输入三个数字，输出最大数
'''


def output_max_of_three():
    num1 = input('请输入第一个数字：')
    num2 = input('请输入第二个数字：')
    num3 = input('请输入第三个数字：')
    print('三个数字分别是：{},{},{}'.format(num1, num2, num3))
    # 直接用max()函数
    # print('三个数字中的最大值是:{}'.format(max(num1, num2, num3)))
    # TODO
    # 用if-else

# output_max_of_three()
