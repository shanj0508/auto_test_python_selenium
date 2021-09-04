# 时间日期模块
'''
时间日期模块一般用于日志、测试报告、订单生产等
时间戳：是从某一个时间点到另一个时间点之间相间隔的秒数.
每个时间戳都以自从 1970 年 1 月 1 日午夜（历元）经过了多长时间来表示。
时间间隔是以秒为单位的浮点小数。

'''

# 导包
import calendar
import datetime
import time

# 获取当前时间戳 time.time()
print('当前时间戳：', time.time())  # 1630393692.5937042

#   时间元组：
#   用9个数字表示，放在元组中  格式：(年,月,日,时,分,秒,一周的第几天(0-6，0表示周一),一年的第几天,夏令时)
t = (2021, 8, 31, 15, 12, 31, 1, 234, 0)
print(t)

# 获取当前时间元组
print('当前时间元组：', time.localtime())
print('当前时间元组：', time.localtime(time.time()))
# 当前时间元组： time.struct_time(tm_year=2021, tm_mon=8, tm_mday=31, tm_hour=15, tm_min=14, tm_sec=23, tm_wday=1, tm_yday=243, tm_isdst=0)

# 获取指定时间元组
print('某一个时间戳对应时间元组：', time.localtime(1630393692.5937042))
# 某一个时间戳对应时间元组： time.struct_time(tm_year=2021, tm_mon=8, tm_mday=31, tm_hour=15, tm_min=8, tm_sec=12, tm_wday=1, tm_yday=243, tm_isdst=0)

# 时间元组转换为时间格式 time.asctime()
print('获取当前时间元组：', time.localtime())
# 获取当前时间元组： time.struct_time(tm_year=2021, tm_mon=8, tm_mday=31, tm_hour=15, tm_min=20, tm_sec=45, tm_wday=1, tm_yday=243, tm_isdst=0)
print('时间元组转换时间格式：', time.asctime(time.localtime()))  # 时间元组转换时间格式： Tue Aug 31 15:20:45 2021

# 格式化当前系统时间：  time.strftime()
print('当前系统时间：', time.strftime('%Y-%m-%d %H:%M:%S'))  # 当前系统时间： 2021-08-31 15:24:24

# 元组转为时间戳 time.mktime()
# 指定时间转为时间戳
print('指定时间转为时间戳：', time.mktime((2020, 3, 12, 0, 0, 0, 0, 0, 0)))  # 指定时间转为时间戳： 1583942400.0
# 当前时间转为时间戳
print('当前时间转为时间戳:', time.mktime(time.localtime()))  # 当前时间转为时间戳: 1630394957.0

# 时间戳转为元组
print('当前时间元组：', time.time(), time.localtime(time.time()))

# 指定日期转为时间格式  datetime.datetime.strptime()
time_str = '2021-04-01 15:23:42'
print(datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S'))  # 2021-04-01 15:23:42

# calendar 模块  日历年历和月历
# 年历
print(calendar.calendar(2021))
'''打印结果：
                                  2021

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7       1  2  3  4  5  6  7
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       8  9 10 11 12 13 14
11 12 13 14 15 16 17      15 16 17 18 19 20 21      15 16 17 18 19 20 21
18 19 20 21 22 23 24      22 23 24 25 26 27 28      22 23 24 25 26 27 28
25 26 27 28 29 30 31                                29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
          1  2  3  4                      1  2          1  2  3  4  5  6
 5  6  7  8  9 10 11       3  4  5  6  7  8  9       7  8  9 10 11 12 13
12 13 14 15 16 17 18      10 11 12 13 14 15 16      14 15 16 17 18 19 20
19 20 21 22 23 24 25      17 18 19 20 21 22 23      21 22 23 24 25 26 27
26 27 28 29 30            24 25 26 27 28 29 30      28 29 30
                          31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
          1  2  3  4                         1             1  2  3  4  5
 5  6  7  8  9 10 11       2  3  4  5  6  7  8       6  7  8  9 10 11 12
12 13 14 15 16 17 18       9 10 11 12 13 14 15      13 14 15 16 17 18 19
19 20 21 22 23 24 25      16 17 18 19 20 21 22      20 21 22 23 24 25 26
26 27 28 29 30 31         23 24 25 26 27 28 29      27 28 29 30
                          30 31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7             1  2  3  4  5
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       6  7  8  9 10 11 12
11 12 13 14 15 16 17      15 16 17 18 19 20 21      13 14 15 16 17 18 19
18 19 20 21 22 23 24      22 23 24 25 26 27 28      20 21 22 23 24 25 26
25 26 27 28 29 30 31      29 30                     27 28 29 30 31

'''
# 月历
print(calendar.month(2021,8))
'''打印结果：
    August 2021
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
'''

# 局部变量 and  全局变量
# 局部变量：定义在方法内部
# 全局变量：定义在方法外部

