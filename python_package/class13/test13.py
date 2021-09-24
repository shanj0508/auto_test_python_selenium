from python_package.class13 import demodef

# 查询
# query = demodef.mysql_query('select * from dept')
# print(query)

# 增加
# insert = demodef.mysql_update('insert into dept(name) values("测试部1")')
# print(insert)


from python_package.class13.demodef2 import my_db

# 查询
# query = my_db().mysql_query('select * from dept')
# print(query)

# 增加
# insert = my_db().mysql_update('insert into dept(name) values("测试部2")')
# print(insert)

from python_package.class13.demodef3 import my_db

a = my_db('db.ini', 'TEST_DB')
b = a.select_query('select * from emp')
print(b)
