# 再来封装日志
# 组件  日志器  处理器  格式器

import logging


def test_log():
    # 创建一个日志器  别的文件使用日志  就用到这个日志器
    logger = logging.getLogger()
    # 设置日志级别  日志信息输出info以上的级别信息  设置了等级但是没有出来info，
    # 原因是：3-5级别底层已经设置了默认在控制台显示，debug和info等级需要手动设置显示在控制台，
    # 因此需要创建控制台，把设置的日志信息放到控制台中
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        #
        # # 设置日志格式 创建一个格式器  日志格式不是我们想要的
        # # 创建一个格式器  设置了格式
        fmt = '%(asctime)s %(filename)s %(levelname)s  %(funcName)s  %(message)s'
        formater = logging.Formatter(fmt)

        # fmt1='%(asctime)s %(filename)s %(levelname)s  %(funcName)s  %(message)s'
        # formater1=logging.Formatter(fmt1)

        # # 处理器 Handler  我要把日志信息输出到哪
        # # 创建一个输出到控制台的处理器  控制台
        sh = logging.StreamHandler()
        # # 把设置的日志信息放到控制台中
        logger.addHandler(sh)
        # 控制台设置格式器
        sh.setFormatter(formater)
        # 在文件里面生成日志信息  创建处理器  文件处理器  处理器的作用：把日志信息输出到指定的位置
        # 文件处理器创建  你的日志信息存放在哪
        fh = logging.FileHandler('log1.log', encoding='utf-8')
        # 需要把日志信息放到文件处理器里面去
        logger.addHandler(fh)
        # 给谁设置格式，给fh设置格式,可以在去定义
        fh.setFormatter(formater)
    return logger

# logger.debug('debug模式')
# logger.info('info模式')
# logger.warning('warning模式')
# logger.error('error模式')
# logger.critical('critical模式')

# 1.创建日志器：产生日志信息
# 2.创建处理器：用来指定日志显示到哪些地方，如果要显示在控制台，则创建控制台处理器；如果要显示在文件中，则创建文件处理器
# 3.通过格式器设置日志的格式

# 问题：重复的日志出现  解决日志重复的问题：增加判断

# 1.封装成方法，也可以封装成配置文件  conf ini
# 格式：
# [模块]  日志器  处理器  格式器
# 模块的内容  键值对的方式
# [模块的细节]
# 细节

# logger_xx的细节  设置日志级别  日志处理器
# handlers_xx的细节  输出内容到哪
# formatters_xx的细节  日志格式


# https://cloud.tencent.com/developer/section/1369394
