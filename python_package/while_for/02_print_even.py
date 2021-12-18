# -*- coding: utf-8 -*-
'''打印10以内的偶数'''

# 方式一：
# for i in range(10):
#     if i % 2 == 0:
#         print(i)

# 方式二：
# for i in range(0,10,2):
#     print(i)

# 方式三：
# for i in range(10):
#     if not i % 2:
#         print(i)

# 方式四：
# for i in range(10):
#     if i % 2:
#         continue
#     print(i)

# 方式五：位运算
# for i in range(10):
#     if i & 1:
#         continue
#     print(i)
