# 日志
'''
日志的作用：
    记录系统内的操作，记录系统的运行状态，帮助快速定位问题
日志模块四大组件：
    1.loggers：日志器，提供应用程序代码直接使用的接口
    2.handlers：处理器，用于将日志记录发送到指定的目的位置
    3.formatters：格式器，用于控制日志信息的最终输出格式
    4.filters：过滤器，提供更细粒度的日志过滤功能，用于决定哪些日志记录将会被输出（其它的日志记录将会被忽略）

日志级别：能够反映出问题的严重程序
    1.debug:调试级别
    2.info:正常的级别
    3.warning:警告，表示程序有问题，但是不影响程序正常运行
    4.error:错误，表示程序有问题，需要修复
    5.critical:严重的问题，程序崩溃，需要修复
'''

# 日志的引入：logging模块是自带的，不需要安装
import logging

# level设置日志级别,format设置日志格式,filename指定日志信息输出到哪个文件中
# basicConfig基础配置写法：1.日志信息不能在控制台和文件里面同时出现；2.会乱码
# fmt = '%(asctime)s %(filename)s %(levelname)s  %(funcName)s  %(message)s'
# logging.basicConfig(level=logging.DEBUG, format=fmt, filename='log1.log')
# 应用日志
# logging.debug('debug模式')
# logging.info('info模式')
# logging.warning('warning模式')
# logging.error('error模式')
# logging.critical('critical模式')

'''输出日志结果：
WARNING:root:warning模式
ERROR:root:error模式
CRITICAL:root:critical模式
'''
# 这里只打印了三条日志信息，分别是日志级别3-5，原因是：默认的日志级别是3，因此只打印大于3的日志信息，debug和info级别不打印
# 若想打印debug和info级别，需要设置日志级别为1，语法：  logging.basicConfig(level=logging.DEBUG)

'''日志格式字符串：
%(asctime)s	日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896
%(created)f	日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值
%(relativeCreated)d	日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的）
%(msecs)d	日志事件发生事件的毫秒部分
%(levelname)s	该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
%(name)s	所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
%(message)s	日志记录的文本内容，通过 msg % args计算得到的
%(pathname)s	调用日志记录函数的源码文件的全路径
%(filename)s	pathname的文件名部分，包含文件后缀
%(module)s	filename的名称部分，不包含后缀
%(lineno)d	调用日志记录函数的源代码所在的行号
%(funcName)s	调用日志记录函数的函数名

'''


# 应用别人封装好的日志组件
# import loguru
#
# loguru.logger.info('info')

# 2021-10-08 10:50:55.897 | INFO     | __main__:<module>:60 - info


# 封装日志函数:该函数的内容就是设置日志的格式，以及指定日志保存的文件路径

def test_log():
    fmt = '%(asctime)s %(filename)s %(levelname)s  %(funcName)s  %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=fmt, filename='log1.log')
    return logging
