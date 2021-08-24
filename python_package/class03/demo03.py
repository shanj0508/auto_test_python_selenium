'''
数据类型：
    1.可变数据类型：
        -字典 dict
        -列表 list
        -集合 set
'''

'''
列表list:
    是一种有序的集合，可以对数据进行增删改，使用最频繁的一种数据类型，相当于数组。
    通过[]进行标识，[]内可以存放任意类型的数据，数据之间用逗号,隔开
'''
# 创建一个空列表
list1 = []
print(list1, type(list1))  # [] <class 'list'>
# 创建多个数据的列表
list2 = [1, 2, 3, 'hello', True, (4, False, 'world')]
print(list2, type(list2))  # [1, 2, 3, 'hello', True, (4, False, 'world')] <class 'list'>

# 访问列表中的数据,通过索引访问,索引从0开始
list3 = [1, 2, 3, 'hello', True, (4, False, 'world')]
print(list3[0])  # 1
print(list3[3])  # hello
print(list3[5])  # (4, False, 'world')
# 列表中使用切片
print(list3[0:3])  # [1, 2, 3]
print(list3[3:])  # ['hello', True, (4, False, 'world')]
# print(list3[6])  # IndexError: list index out of range  索引越界

# 列表的增删改
list4 = [1, 2.3, 'hello', True, (4, False, 'world')]
# 增加
# append():往末尾增加一条数据
list4.append('5')
print(list4)  # [1, 2.3, 'hello', True, (4, False, 'world'), '5']
# insert()：在指定位置增加数据  insert(指定索引,增加的元素)会在指定索引的位置上增加对应元素
list4.insert(2, 'add')  # 在索引为2的位置增加元素add
print(list4)  # [1, 2.3, 'add', 'hello', True, (4, False, 'world'), '5']
# extend():在列表末尾增加数据
list4.extend('add')
print(list4)  # [1, 2.3, 'add', 'hello', True, (4, False, 'world'), '5', 'a', 'd', 'd']
# append() v.s. extend()
# append直接插入对象，extend讲对象拆分成多个后再插入
list4.append([0, 1, 2])
print(list4)  # [1, 2.3, 'add', 'hello', True, (4, False, 'world'), '5', 'a', 'd', 'd', [0, 1, 2]]

list4.extend([0, 1, 2])
print(list4)  # [1, 2.3, 'add', 'hello', True, (4, False, 'world'), '5', 'a', 'd', 'd', [0, 1, 2], 0, 1, 2]

# 修改  通过索引进行修改,索引从0开始
list5 = [1, 2.3, 'hello', True, (4, False, 'world')]
list5[2] = 'xiaoming'
print(list5)  # [1, 2.3, 'xiaoming', True, (4, False, 'world')]
# 删除  pop  remove  del
list6 = [1, 2.3, 'hello', True, (4, False, 'world')]
# pop():通过索引删除,并且会返回被删除的数据
# print(list6.pop(2))  # hello
# print(list6)  # [1, 2.3, True, (4, False, 'world')]
# pop()不填写参数时，默认删除最后一个数据
# print(list6.pop())  # (4, False, 'world')
# print(list6)  # [1, 2.3, 'hello', True]

# remove():指定数据删除  ()内必须填写数据,而不是索引，返回值为None
print(list6.remove('hello'))  # None
print(list6)  # [1, 2.3, True, (4, False, 'world')]

# del()：删除一个元素或者删除连续几个元素或者整个元素删除
# 删除一个元素
list7 = [1, 2.3, 'hello', True, (4, False, 'world')]
# del list7[0]
# print(list7)  # [2.3, 'hello', True, (4, False, 'world')]
# 删除多个元素--通过切片 左闭右开
del list7[1:3]
print(list7)  # [1, True, (4, False, 'world')]
# 删除全部元素
# del list7
# print(list7)  # NameError: name 'list7' is not defined  提示list7未定义，表示list7已经被删除


# 练习：有重复的元素怎么删除
list8 = [1, 2.3, 1, 'hello', False, (4, True, 'world')]
#   1.统计一下重复的元素 count(数据)
print(list8.count(1))  # 统计数字1出现的次数   输出：2
#   2.找到重复元素对应的下标进行删除，可以通过find()或者index()实现    参数为：(目标元素，开始索引，结束索引)
#   区别：find()函数若没有找到匹配的元素，返回-1；  index()函数如果没有找到匹配的元素，会报错。
# index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
# find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
res = list8.index(1, 0, len(list7))
print(res)  # 只会返回第一个匹配的索引   输出：0
print(list8.pop(res))  # 1
print(list8)  # [2.3, 1, 'hello', False, (4, True, 'world')]

# 扩展
# list9 = [1, 2.3, 1, 2.3, 'hello', False, (4, True, 'world')]
# print(max(list9, key=list9.count))


# list运算符 +拼接 *复制
list9 = [1, 2.3, 'hello', False, (4, True, 'world')]
list10 = [4, 5, 'a']
print(list9 + list10)  # [1, 2.3, 'hello', False, (4, True, 'world'), 4, 5, 'a']
print(list10 * 2)  # [4, 5, 'a', 4, 5, 'a']

# list排序
list11 = [9, 3, 2, 6, 1, 8]
#   升序
# list11.sort()
# print(list11)  # [1, 2, 3, 6, 8, 9]
#   降序
# list11.sort(reverse=True)
# print(list11)  # [9, 8, 6, 3, 2, 1]
# 翻转
list11.reverse()
print(list11)  # [8, 1, 6, 2, 3, 9]

# 数据类型转换
#   元组转为列表 list()
tup1 = (1, 'a', False)
print(list(tup1), type(list(tup1)))  # [1, 'a', False] <class 'list'>
#   列表转为元组 tuple()
list12 = [1, 'a', False]
print(tuple(list12), type(tuple(list12)))  # (1, 'a', False) <class 'tuple'>

'''
字典dict:
    也是用来存储数据，是除了列表以外最灵活的数据结构
    通过{}进行标识，格式：{key1:value1,key2:value2,...}  
    用多个键值对来表示，其中key是唯一的。
'''
# 创建一个空字典
dic1 = {}
print(dic1, type(dic1))  # {} <class 'dict'>
# 创建一个有数据的字典
dic1 = {'name': '小红', 'age': 18}
print(dic1)  # {'name': '小红', 'age': 18}

# 访问字典中的数据：通过键的方式去访问
dic2 = {'name': '小红', 'age': 18}
print(dic2['name'])  # 小红
print(dic2['age'])  # 18

# 字典的增删改
#   增加数据
dic3 = {'name': '小红', 'age': 18}
dic3['gender'] = '女'
print(dic3)  # {'name': '小红', 'age': 18, 'gender': '女'}
#   修改数据
dic3['name'] = '小明'
print(dic3)  # {'name': '小明', 'age': 18, 'gender': '女'}
#   删除数据
#   pop()指定键删除；
dic5 = {'name': '小红', 'age': 18, 'gender': '女'}
dic5.pop('name')
print(dic5)  # {'age': 18, 'gender': '女'}

#   popitem()删除最后一个；
dic6 = {'name': '小红', 'age': 18, 'gender': '女'}
dic6.popitem()  # {'name': '小红', 'age': 18}
print(dic6)
#   del[]指定键删除或者删除全部
# dic4 = {'name': '小红', 'age': 18, 'gender': '女'}
# del dic4['gender']
# print(dic4)  # {'name': '小红', 'age': 18}
# del dic4
# print(dic4)  # NameError: name 'dic4' is not defined  dic4未定义表示已经被删除


# update更新字典数据:  键不能重复,若键名相同，则更新数据，若键名不同，则增加数据
dic7 = {'name': '小红', 'age': 18}
dic8 = {'name': '小明', 'age': 19, 'gender': '男', }
dic7.update(dic8)
print(dic7)  # {'name': '小明', 'age': 19, 'gender': '男'}

# 字典转换数据类型
# 字典转为字符串
dic9 = {'name': '小红', 'age': 18}
print(dic9, type(dic9))  # {'name': '小红', 'age': 18} <class 'dict'>
print(str(dic9), type(str(dic9)))  # {'name': '小红', 'age': 18} <class 'str'>
# 字符串转为字典 eval()
str1 = "{'name': '小红', 'age': 18}"
print(str1, type(str1))  # {'name': '小红', 'age': 18} <class 'str'>
print(eval(str1), type(eval(str1)))  # {'name': '小红', 'age': 18} <class 'dict'>

# items() 一次性拿到字典中所有的值
dic10 = {'name': '小红', 'age': 18}
for i, j in dic10.items():
    print(i, j)  # name 小红  age 18

# 创建一个新的字典 fromkeys(键列表，值)
dic11 = {}
list13 = ['name', 'age', 'gender']
dic12 = dic11.fromkeys(list13, 1)
print(dic12)  # {'name': 1, 'age': 1, 'gender': 1}

'''
集合set:
    是无序的。
    通过{}或者set进行标识
    集合里面的数据可以是任意类型的。
'''
# 创建一个集合
#   1.{}---推荐使用这种方式
set1 = {1, 2, 3.5, '小红'}
print(set1, type(set1))  # {1, 2, 3.5, '小红'} <class 'set'>
#   2.set()
set2 = set((1, 2, 3.5, '小明'))
print(set2, type(set2))  # {'小明', 1, 2, 3.5} <class 'set'>
# 创建空集合必须使用set来创建,因为dict也是通过{}作为标识符，因此通过{}创建空时默认是dict类型
set3 = {}
print(set3, type(set3))  # {} <class 'dict'>
set4 = set()
print(set4, type(set4))  # set() <class 'set'>

# 访问set中的元素：不能访问set中的元素，因为set中元素是无序的

# set进行增删改
# 增加 add()
set5 = set((1, 2, 3.5, '小明'))
set5.add('hello')
print(set5)  # {1, 2, 3.5, 'hello', '小明'}
# 修改 update()
set6 = set((1, 2, 3.5, '小明'))
set6.update('小红')
print(set6)  # {1, 2, 3.5, '小明', '红', '小'}
# 删除
# remove():指定元素删除,若没有找到该元素，会报错KeyError:
set7 = set((1, 2, 3.5, '小明'))
set7.remove('小明')
print(set7)  # {1, 2, 3.5}
set7.remove(3.5)
print(set7)  # {1, 2}
# pop()：任意删除一个元素
set8 = set((1, 2, 3.5, '小明'))
set8.pop()
print(set8)  # {2, 3.5, '小明'}  {1, 2, 3.5}
# discard()：指定元素删除,若没有找到该元素，不会报错
set9 = set((1, 2, 3.5, '小明'))
set9.discard('小明')
print(set9)  # {1, 2, 3.5}
# clear()：删除所有元素
set10 = set((1, 2, 3.5, '小明'))
set10.clear()
print(set10)  # set()

# set的应用场景:对集合进行操作，对重复数据进行操作
# 交集&：两个集合中相同的元素
# 并集|：两个集合中所有的元素，去重
# 差集-：A-B表示集合A中所有的元素，减去与B重复的元素
# 补集^：返回两个集合中所有的元素，减去两个集合的重复元素
set1 = {1, 2, 3, 4, 5}
set2 = {5, 6, 7, 8}
print(set1 & set2)  # {5}
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8}
print(set1 - set2)  # {1, 2, 3, 4}
print(set1 ^ set2)  # {1, 2, 3, 4, 6, 7, 8}

# set去重复
a = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(a)  # [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(set(a))  # {1, 2, 3, 4, 5}
# for循环打印不换行
for i in set(a):
    print(i,end='')  # 12345
