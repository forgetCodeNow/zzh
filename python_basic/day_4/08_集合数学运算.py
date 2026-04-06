# 并集 交集 差集 对称差集

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7, 8, 9}

# 并集：把集合合并
s3 = s1 | s2
print(s3)

# 交集：取出集合中重复的元素
s4 = s1 & s2
print(s4)

# 差集：取出s1不属于s2的元素，和方法setA.difference_update(setB)同理，但是方法setA.difference_update(setB)是作用在原集合上
s5 = s1 - s2
print(s5)

# 对称差集：取两个集合不相交的元素
s6 = s1 ^ s2
print(s6)