d1 = {'name': 'zhangsan', 'age': 22, 'father': 'lisi'}

# 查询 方法一 直接取值，如果取值的key不存在，会报错
print(d1['name'])
# print(d1['mother'])  # 没有mother key报错

# 查询 方法二 安全取值，dict.get(key) 如果取值的key不存在，返回默认值，没有设置默认值就返回None
print(d1.get('name'))
print(d1.get('mother'))
print(d1.get('mother', '没有这个key'))


# 新增 直接增
d1['mother'] = 'xiaofang'
print(d1)

# 修改 方法一 直接修改，跟新增方法一样,key存在则修改，不存在则新增
d1['age'] = 18
print(d1)

# 修改方法二 批量修改，dict.update(dict)，同样，key不存在则新增
d1.update({'name': 'wangwu', 'age': 33})
print(d1)
d1.update({'name': 'zhangsan', 'age': 22, 'school': 'diyizhongxue'})
print(d1)

# 删除 方法一 删除指定key的键值对
del d1['mother']
print(d1)

# 删除 方法二 删除指定key的键值对，并返回value
result = d1.pop('school')
print(result)
print(d1)
# dict.pop(key,'默认值') 当key不存在时，返回默认值,如果不写默认值会报错
result2 = d1.pop('school','key不存在')  # 返回key不存在
print(result2)

# 删除 方法三 清空字典
d1.clear()