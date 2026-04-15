# Python中操作文件的标准流程
# 1、创建文件对象
# 2、操作文件（读、写） 读取到最后，继续读取的值是空字符串
# 3、关闭文件

# 打开文件
file = open(file='a.txt', mode='rt', encoding='utf-8')

# 读取文件方法一
# size参数，读取的字符数，会记住读取位置
# print(file.read(1))
# result = file.read()
# print(result)

# 读取方法二
# 按行读取，一样有size参数，读取的字符数，会记住读取位置
# 通常和while循环一起使用
# while True:
#     line = file.readline()
#     if not line:
#         break
#     print(line,end='')

# 读取方法三
# readlines 一次性按行读取完整个文件,返回一个列表
# hint参数：期望读取的【字符个数 或字节数的上限】(hint不是行数)
result = file.readlines(10)
print(result)


#关闭文件
file.close()


# with 使用：上下文管理器，结合for循环，逐行读取文件
# with代码体执行结束后会自动关闭文件
with open(file='a.txt', mode='rt', encoding='utf-8') as f:
    for line in f:
        print(line,end='')
