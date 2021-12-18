# -*- coding: utf-8 -*-
'''
    给定一个不超过5位的正整数，判断该数的位数，依次打印出个位、十位、百位、千位、万位的数字
'''


# 方式一：通过str格式打印
def print_integer_digits1():
    flag = True
    digits = ['个位', '十位', '百位', '千位', '万位']
    while flag:
        try:
            # 1.用户输入数字
            input_num = int(raw_input('请输入一个5位的正整数：'))
            # 2. 获取输入数字的长度
            input_num_str = str(input_num)
            input_num_length = len(input_num_str)
            # 3. 判断数字是5位的正整数
            if input_num <= 0:
                print('------输入不合法,请重新输入------')
            else:
                if input_num_length > 5:
                    print('------输入不合法,请重新输入------')
                else:
                    print('输入合法,输入的数字是：{},这是一个{}位数'.format(input_num, input_num_length))
                    # 1. 从高位到低位打印
                    # for i in range(input_num_length):
                    #     print('{}:{}'.format(digits[i], input_num_str[i]))
                    # 2. 从低位到高位打印
                    # 字符串反转
                    input_num_str = input_num_str[::-1]
                    for i in range(input_num_length):
                        print('{}:{}'.format(digits[i], input_num_str[i]))

                    flag = False
        except ValueError:
            print('------输入不合法,请重新输入------')

        except Exception as e:
            print('发生未知错误：{}'.format(e))


# 方式二：通过int格式打印
def print_integer_digits2():
    flag = True
    digits = ['个位', '十位', '百位', '千位', '万位']
    input_num_length = 0

    while flag:
        try:
            # 1.用户输入数字
            input_num = int(raw_input('请输入一个5位的正整数：'))
            # 2. 判断数字是5位以内的正整数
            if input_num <= 0:
                print('------输入不合法,请输入一个正整数------')
            elif input_num >= 100000:
                print('------输入不合法,请输入五位以内的正整数------')
            else:
                # 3. 获取输入数字的长度
                if input_num >= 1000:
                    if input_num >= 10000:
                        input_num_length = 5
                    else:
                        input_num_length = 4
                else:
                    if input_num_length >= 100:
                        input_num_length = 3
                    elif input_num_length >= 10:
                        input_num_length = 2
                    else:
                        input_num_length = 1
                print('输入合法,输入的数字是：{},这是一个{}位数'.format(input_num, input_num_length))
                num = input_num
                # 1.1 从高位到低位打印
                pre_num = 0
                for i in range(input_num_length, 0, -1):
                    cur_num = num // 10 ** (i - 1)
                    digits_num = cur_num - pre_num * 10
                    print('{}:{}'.format(digits[i - 1], digits_num))
                    pre_num = cur_num

                # 2.1 从低位到高位打印
                # for i in range(input_num_length):
                #     n = num // 10
                #     digits_num = num - n * 10
                #     print('{}:{}'.format(digits[i], digits_num))
                # ！这里必须赋值！
                #     num = n
                # 2.2 从低位到高位打印
                # num *= 10
                # i = 0
                # while num // 10 != 0:
                #     num //= 10
                #     digits_num = num % 10
                #     print('{}:{}'.format(digits[i], digits_num))
                #     i += 1
                # 2.3. 从低位到高位打印
                # for i in range(input_num_length):
                #     digits_num = num % 10
                #     print('{}:{}'.format(digits[i], digits_num))
                #     num //= 10

                flag = False
        except ValueError:
            print('------输入不合法,请输入数字------')

        except Exception as e:
            print('发生未知错误：{}'.format(e))


if __name__ == '__main__':
    print_integer_digits2()
