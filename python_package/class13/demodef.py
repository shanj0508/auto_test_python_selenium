import pymysql

def mysql_query(sql):
    # 1.连接数据库
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='test01')
    # 2.创建游标:curson，类似于指针
    cur = con.cursor()
    # 3.操作数据库：
    # 查询
    # sql = 'select * from dept'
    cur.execute(sql)
    # 打印查询结果
    resAll = cur.fetchall()
    # 4.操作完成后关闭数据库
    con.close()
    return resAll

def mysql_update(sql):
    # 1.连接数据库
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='test01')
    # 2.创建游标:curson，类似于指针
    cur = con.cursor()
    # 3.操作数据库：
    cur.execute(sql)
    cur.execute('commit')  # 增删改需要commit,查询不需要
    # 4.操作完成后关闭数据库
    con.close()
    return True