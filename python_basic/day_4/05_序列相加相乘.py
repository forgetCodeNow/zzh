# 序列相加,容器拼接
list1 = [1,2,3,4]
list2 = [5,6,7,8]
str1 = 'hello'
str2 = 'world'

list3 = list1 + list2
str3 = str1 + str2
print(list3)
print(str3)

# 序列相乘,相当于容器复制多次，返回新的容器，原容器不会修改
list4 = list1 * 3
str4 = str3 * 3
print(list4)
print(str4)