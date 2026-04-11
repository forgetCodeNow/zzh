# 1、map函数：对一组数据中的每个元素进行统一加工，返回一组新的数据，原数据不变
# map(操作函数，可迭代对象)
nums = [1, 2, 3, 4, 5]
# map函数返回值是迭代器对象，需要手动遍历或者类型转换
result = map(lambda num: num + 5,  nums)
print(list(result))
print(list(result))     # 结果是空列表，因为上一行已经把map结果耗尽了
'''
注意点
1、延迟执行：map不会立刻计算，只用在需要结果的时候才计算（遍历、类型转换时）
2、返回的是迭代器对象，且一旦遍历完成，就会被耗尽
3、map不会影响元素数量
'''


# 2、filter函数：对一组数据中的，筛选出符合条件的元素，返回一组新的数据，原数据不变
# filter(过滤函数，可迭代对象)
nums = [1, 2, 3, 4, 5]

result = filter(lambda num: num > 3, nums)
print(list(result))

# 筛选成年人
persons = [
    {'name': 'zhangsan', 'age': 22},
    {'name': 'lisi ', 'age': 12},
    {'name': 'wangwu', 'age': 33},
    {'name': 'tiedan', 'age': 4}
]
result_adult = filter(lambda person: person['age'] >= 18, persons)
print(list(result_adult))

# filter特殊用法，不使用过滤函数，默认过滤假值=False的值
strs = ['w','y', 'z', '', None, 0 , 3, [], ()]
result2 = filter(None, strs)
print(list(result2))


'''
注意点
1、延迟执行：filter不会立刻计算，只用在需要结果的时候才计算（遍历、类型转换时）
2、返回的是迭代器对象，且一旦遍历完成，就会被耗尽
3、filter可能会影响元素数量
'''

# 3、sorted函数:对一组数据进行排序，返回一组新数据
# sorted(可迭代对象，key=排序条件函数，reverse=bool)
# 数字排序
nums = [20, 444, 23, 2, 1]
result = sorted(nums)
print(result)

# 根据字符串长度排序
strs = ['python', 'c', 'java']
result2 = sorted(strs, key=len)
print(result2)

# 根据字典中某个字典排序
persons = [
    {'name': 'zhangsan', 'age': 22},
    {'name': 'lisi ', 'age': 12},
    {'name': 'wangwu', 'age': 33},
    {'name': 'tiedan', 'age': 4}
]
result3 = sorted(persons, key=lambda item: item['age'])
print(result3)

# 4、reduce函数:将一组数据不断合并，最终归并成一个结果
# reduce(合并函数，可迭代对象，初始值)
# 注意：reduce函数需要导入functools模块

from functools import reduce
# 数字操作
nums = [20, 444, 23, 2, 1]
result = reduce(lambda x, y: x + y, nums)
print(result)

# 字符串拼接操作
strs = ['python', 'c', 'java']
result2 = reduce(lambda x, y: x + y, strs, 'basic')
print(result2)