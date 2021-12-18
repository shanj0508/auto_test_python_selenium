# -*- coding: utf-8 -*-
'''计算1000以内被7整除的前20个数'''

# 方式一：
# count = 0
# for i in range(1000):
#     if i % 7 == 0:
#         count += 1
#         if count <= 20:
#             print(i)

# 方式二：
count = 0
for i in range(0, 1000, 7):
    print(i)
    count += 1
    if count >= 20:
        break
