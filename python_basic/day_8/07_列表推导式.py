# 列表推导式本质上是对 for循环+append的一种简写
# 语法格式：[表达式 for 变量 in 可迭代对象]

# 让列表中的每个元素*2，得到一个新列表
nums = [20, 30, 40]
# 方法一 map
result = list(map(lambda num: num*2, nums))
print(result)

# 方法二 列表推导式
result2 = [n * 2 for n in nums]
print(result2)

# 带条件的列表推导式
result3 = [n * 2 for n in nums if n > 20]
print(result3)

# 字典推导式
names = ['zhangsan', 'lisi', 'wangwu']
scores = [90, 80, 70]
result4 = {names[i]: scores[i] for i in range(len(names))}
print(result4)

# 集合推导式
result5 = {n+ '!' for n in names}
print(result5)

# 没有元组推导式