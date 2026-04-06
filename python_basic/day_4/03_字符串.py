str1 = 'hello'

# 字符串可以用下标读取字符串元素,字符串中的字符不能修改
print(str1[0])

# 字符串不能嵌套
# str2 = 'hello 'nihao' python'  报错invalid syntax


# 常用方法
# 方法一 str.index() 查找指定元素的在字符串中第一次出现下标
print(str1.index('l'))

# 方法二 str.split() 按字符串指定元素将字符串分割，生产一个新的列表，原字符串不做改变
str1_split = str1.split('l')
print(str1_split)
str1_split2 = str1.split('w')   # 如果字符串中没有该指定元素，则返回一个单一元素列表
print(str1_split2)

# 方法三 str.count()统计指定字符在字符串中出现的次数
str1_count = str1.count('l')
print(str1_count)

# 方法四 str.replace() 将字符串某个字段替换成目标字符串
str1_replace = str1.replace('ll', 'ww')
print(str1_replace)
str1_replace2 = str1.replace('xx', '**')    # 替换字符片段不存在时，不会对字符串做更改
print(str1_replace2)

# 方法五 str.strip() 从某个字符串中删除指定字符串中任意字符
# 删除规则：从字符串的两端开始删除,知道遇到第一个不在指定字符串中的字符就停下
# 不传参数默认删除空格
str1_strip = str1.strip('o')
print(str1_strip)
str1_strip2 = str1.strip('ho')
print(str1_strip2)