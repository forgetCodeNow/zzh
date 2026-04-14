# 1、能被for循环遍历的对象就是可迭代对象（iterable）
nums = [10, 20, 30]
names = ('zhangsan','lis')
for name in names:
    print(name)

# 2、可迭代对象能调用__iter__()方法
names_it = names.__iter__()

# 3、调用__iter__()方法就会得到一个迭代器（iterator）
# 备注1、__iter__()是魔法方法，使用iter()函数会自动调用
# 备注2、nams.__iet__() 等价于 iter(names)
# 备注3、如果iter(obj)能得到一个迭代器，那么obj就是一个可迭代对象
print(type(names_it))   # <class 'tuple_iterator'>
nums_it = iter(nums)
print(type(nums_it))    # <class 'list_iterator'>

# 4、迭代器有__next__()方法，每次调用会根据当前状态返回下一个元素
# 备注1、__next__()也是魔法方法，等价于next()
# 备注2、当所有元素都取出后，继续调用next()方法，会抛出StopIteration异常
try:
    print(next(names_it))
    print(next(names_it))
    print(next(names_it))    # 这条会抛出异常
except StopIteration as e:
    print('迭代器已全部取出！！！')

# 5、迭代器也有__iter__()方法，返回的值是迭代器本身
result = iter(nums_it)
print(nums_it)      # <list_iterator object at 0x000001DD7150E8C0>
print(result)       # <list_iterator object at 0x000001DD7150E8C0>

for n in result:        # 相当于调用了iter(result)
    print(n)

# 6、迭代器协议
# 1、能被iter()接受
# 2、能被next()一步一步取值