s1 = {1, 2, 3, 4, 5, 2, 3, 4, 5}

# 集合 增加元素方法一 set.add() 增加单个元素
s1.add(10)  # 向s1集合中加入10
print(s1)

# 集合 增加元素方法二 set.update() 批量添加元素，必须传递可迭代对象，如：集合、列表、元组
s1.update({'a', 'b'})
s1.update([110, 112])
print(s1)

# 集合 删除元素方法一 set.remove() & set.discard()，都是删除集合中指定的元素，
# 区别是碰到集合没有的元素时，remove（）会报错，discard（）不会报错
s1.remove(10)
s1.discard(120)  # 实际集合中没有120元素，仍可以正常执行
print(s1)

# 集合 删除元素方法二 set.pop() 随机删除集合元素，并返回
print(s1.pop())
print(s1)

# 集合 删除元素方法三 set,clear() 清空集合
s1.clear()
print(s1)  # 输出结果set()空集合

# 集合 修改元素方法，集合没有直接修改元素的方法，使用remove() + add() 组合实现修改操作
s2 = {1, 2, 3, 4, 5, 2, 3, 4, 5}
s2.remove(5)  # 把5修改成55
s2.add(55)
print(s2)

# 集合 查找元素方法：使用成员运算符来判断查找的元素是否存在集合中
result = 55 in s2
print(result)
result2 = 5 not in s2
print(result2)
