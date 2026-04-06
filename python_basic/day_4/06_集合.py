# 集合定义


'''
 可变集合
 1、无序的，输出不会按创建时的顺序
 2、不能通过下标访问
 3、会自动去重
'''
s1 = {1,2,1,2,3,4,5,6,7}
s2 = {'a','b','c','a','d'}
print(s1)   # 输出结果{1, 2, 3, 4, 5, 6, 7}
print(s2)  # 输出结果{'a', 'd', 'b', 'c'}

# 定义空集合
s_empty = set()  # set() 是唯一定义空集合形式
s_empty_false = {}  # 这个不是空集合，这个是空字典
print(type(s_empty_false))  # 输出结果<class 'dict'>，类型为字典

'''
不可变集合
 1、无序的，输出不会按创建时的顺序
 2、不能通过下标访问
 3、会自动去重
 4、不可改变集合元素，不能增删改
 5、可以接受任意可迭代对象，但返回的都是不可变集合
'''
s3 = frozenset(s1)
s4 = frozenset(s2)
print(s3)  # 输出结果frozenset({1, 2, 3, 4, 5, 6, 7})
print(s4)  # 输出结果frozenset({'b', 'd', 'a', 'c'})

s5 = frozenset(['zeng', 'zi'])
print(s5)  # 输出结果frozenset({'zeng', 'zi'})

# 定义不可变空集合，基本用不上
s_empty_frozen = frozenset()