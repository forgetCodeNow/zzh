s1 = {1, 2, 3, 4, 5, 4, 2, 10}
s2 = {4, 5, 6, 7}

# 集合方法一 setA.difference(setB)
# 作用：找出集合A中，不同于集合B的元素，AB集合不发生改变，返回一个新的集合
s1_s2_difference = s1.difference(s2)
print(s1_s2_difference)
s2_s1_difference = s2.difference(s1)
print(s2_s1_difference)

# 集合方法二 setA.difference_update()
# 作用：从集合A中，删除和集合B相同的元素，直接作用在集合A上
s1.difference_update(s2)
print(s1)

# 集合方法三 setA.union(setB)
# 作用：合并两个集合，不改变AB集合，返回一个新集合
s1_s2_union = s1.union(s2)
print(s1_s2_union)

# 集合方法四 setA.issubset(setB)
# 作用：判断A集合是否为B集合的子集，返回布尔值
s3 = {1, 2, 3}  # 是s1 的子集
is_s2_subset = s1.issubset(s2)
is_s1_subset = s3.issubset(s1)  # 返回结果为True
print(is_s1_subset)
print(is_s2_subset)

# 集合方法五 setA.issuperset(setB)
# 作用：判断A集合是否为B集合的超集，即B是否为A的子集，返回布尔值
is_s3_issuperset = s1.issuperset(s3)  # 返回结果为True
is_s2_issuperset = s1.issuperset(s2)  # 返回结果为False
print(f'is_s2_issuperset:{is_s2_issuperset}')
print(f"is_s3_issuperset:{is_s3_issuperset}")

# 集合方法六 setA.isdisjoint(setB)
# 作用：判断A集合和B集合是否没有交集，返回布尔值
is_s2_isdisjoint = s1.isdisjoint(s2)  # 在第14行代码中删除了s1 s2 的交集，返回结果为True
is_s3_isdisjoint = s1.isdisjoint(s3)  # s3是s1的子集，肯定有交集，返回结果为False
print(f'is_s3_isdisjoint:{is_s3_isdisjoint}')
print(f'is_s2_isdisjoint:{is_s2_isdisjoint}')
