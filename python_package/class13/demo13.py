# python连接数据库
# 安装数据库模块 cmd >>> pip install pymysql

# 引入pymysql
import pymysql

'''操作数据库的步骤：
    1.连接数据库
    2.创建游标:curson，类似于指针
    3.操作数据库
    4.操作完成后关闭数据库
'''

# 1.连接数据库
con = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='test01')
print(con)  # <pymysql.connections.Connection object at 0x000001C92E6E7AF0>

# 2.创建游标:curson，类似于指针
cur = con.cursor()

# 3.操作数据库：
# 增加
# sql = 'insert into dept(id,name) values(10,"测试部")'
cur.execute(sql)
cur.execute('commit')  # 增删改需要commit,查询不需要

# 批量增加数据
# sql = 'insert into dept(name) values(%s)'
# value = ([('研发部1'), ('研发部2')])
# cur.executemany(sql,value)
# cur.execute('commit')  # 增删改需要commit,查询不需要

# 修改
# sql = 'update dept set name="测试部2" where id=10 '
# cur.execute(sql)
# cur.execute('commit')

# 删除
# sql = 'delete from dept where id=10 '
# cur.execute(sql)
# cur.execute('commit')

# 查询
# sql = 'select * from dept'
# cur.execute(sql)
# 打印查询结果
# fetchall()：拿出全部数据
# fetchmany(条数)：指定拿出几条数据
# fetchone()：只会拿出一条数据
# resAll = cur.fetchall()
# print(resAll)  # ((1, '开发部'), (2, '市场部'), (3, '财务部'), (8, '销售部'), (9, None))

# resMany = cur.fetchmany(2)
# print(resMany)  # ((1, '开发部'), (2, '市场部'))

# resOne = cur.fetchone()
# print(resOne)  # (1, '开发部')


# 4.操作完成后关闭数据库
con.close()
