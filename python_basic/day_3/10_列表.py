# 定义空列表
list1 = []
list2 = list()

# 下标索引值,正数索引值从0开始从前往后，负数索引值从-1开始从后往前
list3 = list(range(1,10))
print(list3)
print(list3[2])
print(list3.index(4,3,10))


# 基本操作，增删改查
#新增 方法一 在列表尾部添加
list2.append(1)
# 新增 方法二 在列表指定下标添加元素
list2.insert(3,4)  # 如果超出原有下标，则在列表尾部添加
list2.insert(3,4)
list2.insert(0,4)  # 如果该下标有其他元素，则会被替换
# 新增 方法三 将可迭代对象的内容依次取出,追加到列表尾部
list2.extend(list3)
print(list2)

# 删除 方法一 删除指定位置元素，将该元素返回
list2.pop(0)
pop2 = list2.pop(3)
print(list2)
# 删除 方法二 删除列表第一个出现的指定值，必须是列表里面有的值，没有的值运行会报错
list2.remove(4)
print(list2)
# list2.remove(10)    报错list.remove(x): x not in list
# 删除 方法三 删除列表中的所有元素
list3.clear()
# 删除 方法四 删除指定位置的元素，元素下标不能超过长度
del list2[3]
# del list2[20]       报错list assignment index out of range
print(list2)

# 修改，直接通过元素下标修改
list2[0] += 1
print(list2)

# 查询,通过下标获取指定位置元素
print(list2[0])
