# 只能用for循环
d1 = {'name': 'zhangsan', 'age': 22, 'father': 'lisi'}

for key in d1:
    print(key, d1[key])


for key in d1.keys():
    print(key, d1[key])