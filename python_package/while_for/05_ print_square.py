'''
打印一个边长为n的正方形,例如：
    ***
    * *
    ***
'''


def print_square():
    n = 6
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            row_str = ''
            for j in range(n):
                if j == 0 or j == n - 1:
                    row_str += '*'
                else:
                    row_str += ' '
            else:
                print(row_str)


# print(self, *args, sep=' ', end='\n', file=None)
def print_square2():
    n = 5
    print('*' * n)
    for i in range(n - 2):
        print('*', ' ' * (n - 2), '*', sep='')

    print('*' * n)


def print_square3():
    n = 4
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*', ' ' * (n - 2), '*', sep='')


# range函数对称性
'''
分析：
    边为3,则 -1 0 1 => range(-1,2)
    边为4,则 -2 -1 0 1 => range(-2,2)
    边为5,则 -2 -1 0 1 2 => range(-2,3)
'''


def print_square4():
    n = 5
    e = -n // 2
    for i in range(e, n + e):
        if i == e or i == n + e - 1:
            print('*' * n)
        else:
            print('*', ' ' * (n - 2), '*', sep='')


if __name__ == '__main__':
    print_square4()
