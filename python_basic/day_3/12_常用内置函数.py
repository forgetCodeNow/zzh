# sorted(数据容器,reverse) 对数据进行排序，但不会改变原数据容器,需要变量接收返回值
list1 = [3,5,2,34,5,2,43,543,41324]
list1_sorted = sorted(list1, reverse=True)
print(list1_sorted)

# len() 获取容器中元素的个数，经常在循环中使用
list1_len = len(list1)
print(list1_len)

# max() min()  返回容器中的最大/小值，注意：字符串和数值同时存在时不能用
list1_max = max(list1)
print(list1_max)
list1_min = min(list1)
print(list1_min)
# list1.append('x')
# list1_max = max(list1)   报错'>' not supported between instances of 'str' and 'int'

# sum() 求和函数，注意：字符串不能使用,容器中只能是数值类型
list1_sum = sum(list1)
print(list1_sum)