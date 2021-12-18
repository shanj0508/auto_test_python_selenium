# -*- coding: utf-8 -*-
'''
    求100以内所有的奇数的和（2500）
'''


def print_odd_sum():
    sum = 0
    for i in range(1, 100, 2):
        sum += i
    else:
        print(sum)


def print_odd_sum1():
    sum = 0
    for i in range(100):
        if i % 2:
            sum += i
    else:
        print(sum)


if __name__ == '__main__':
    print_odd_sum1()
