from python_package.class13 import demodef

# 查询
# query = demodef.mysql_query('select * from dept')
# print(query)

# 增加
insert = demodef.mysql_update('insert into dept(name) values("测试部1")')
print(insert)
