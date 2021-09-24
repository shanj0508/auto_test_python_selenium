import pymysql
import configparser


# 这个类专门用来操作数据库的
class my_db:
    # 连接
    def __init__(self, configPath, db):
        # 实例config工具
        config = configparser.ConfigParser()
        # 从配置文件里读取数据库服务器IP  账号 密码.....
        config.read(configPath)
        host = config[db]['host']
        port = int(config[db]['port'])
        user = config[db]['user']
        password = config[db]['password']
        db_name = config[db]['database']
        charset = config[db]['charset']
        try:
            # 1.连接数据库
            self.con = pymysql.connect(host=host, port=port, user=user,
                                       password=password, database=db_name, charset=charset)
        except Exception as e:
            print('初始化数据库连接失败：%s' % e)
        # 2.创建游标:curson，类似于指针
        self.cur = self.con.cursor()

    # 3.操作数据库：
    # 查询
    def mysql_query(self, sql):
        try:
            # 执行sql
            self.cur.execute(sql)
            # 打印查询结果
            result = self.cur.fetchall()
            return result
        except Exception as e:
            print('查询失败%s' % e)

    # 增删改
    def mysql_update(self, sql):
        try:
            # 执行sql
            self.cur.execute(sql)
            # 提交数据
            self.cur.execute('commit')
            return True
        except Exception as e:
            print('增删改失败%s' % e)
            # sql执行增删改失败后要继续回滚
            self.cur.execute('rollback')
