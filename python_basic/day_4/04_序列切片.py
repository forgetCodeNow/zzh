list1 = list(range(1,11))

# 序列切片操作
list2 = list1[0:3:1]
list3 = list1[3:10:2]
print(list1)
print(list2)
print(list3)
list4 = list1[::]   # 表示从头取到尾，步长默认1，相当于复制列表

list5 = list1[::-1]  # 默认起始和结束位置，步长为负数时，起始位置和结束位置对换