# 方法一 dict.keys()，返回字典中所有key
d1 = {'name': 'zhangsan', 'age': 22, 'father': 'lisi'}
result = d1.keys()
print(result)

# keys() 返回值为dict_keys类型，可以遍历，但是不能通过下标访问元素
for item in result:
    print(item)
# print(result[0])  # 执行结果TypeError: 'dict_keys' object is not subscriptable

# 可以通过类型转换成其他类型
str1 = str(result)
print(str1)
print(str1[0])
l1 = list(result)
t1 = tuple(result)
s1 = set(result)
print(l1)
print(t1)
print(s1)


# 方法二 dcit.values() 获取字典中所有的value
# values() 返回值为dict_values类型，可以遍历，但是不能通过下标访问元素
result2 = d1.values()
print(result2)

# 方法三 dict.items() 获取所有键值对
# 返回值为dict_items类型，和dict_keys一样
result3 = d1.items()
print(result3)

