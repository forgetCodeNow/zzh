# index() 返回列表指定值的下标，必须是列表中存在的元素，否则报错，不会进入嵌套列表中查找
list1 = list(range(1,10))
index_6 = list1.index(6)
print(index_6)

# count() 通知指定值在列表中出现的次数,元素不存在时，返回0，不会报错,不会进入嵌套列表中查找
list2 = list1.copy()
list2.extend(list1)
print(list2.count(6))   # 统计list2列表中元素6出现的次数

# reverse() 反转列表,首尾颠倒，在原列表上直接操作，没有返回值
list2.reverse()
print(list2)

# sort(reverse = bool) 对列表进行排序，默认从小到大，可以用参数reverse改变,在原列表上直接操作，没有返回值;
# 注意：列表中字符串和数字同时存在时，sort()方法不可用，会报错
list1.sort(reverse=True)
print(list1)