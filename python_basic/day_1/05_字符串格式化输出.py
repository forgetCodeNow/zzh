name = 'zhangsan'
age = 18
weight = 77.7

# 方法一 使用加号拼接字符串，只能字符串拼接
info_1 = '我是' + name

# 方法二 使用占位符
info_2 = '我是%s,今年%d岁，体重%.2f公斤' % (name,  age, weight)

print(info_2)

# 方法三 format() str.format()
info_3 = '我是{1},今年{0}岁，体重{2}公斤'.format(age, name , weight)

print(info_3)

#方法四 使用f-string
info_4 = f'我是{name},今年{age}岁，体重{weight+1}公斤'

print(info_4)

# 占位符精度控制
info_5 = '我是%s,今年%0.4d岁，体重%.2f公斤' % (name,  age, weight)

print (info_5)