# w：写入，先清空文件内容,文件不存在则创建
with open(file='a.txt', mode='w', encoding='utf-8') as f:
    f.write('hello')

# x：排他性创建，如果文件已经存在，则创建失败，抛出异常,仅可写入文件
try:
    with open(file='demo2.txt', mode='x', encoding='utf-8') as f:
        f.write('hello')
except FileExistsError as e:
    print(e)

# a：打开文件用于写入，如果文件存在，则在文件末尾追加
with open(file='a.txt', mode='a', encoding='utf-8') as f:
    f.write('Python')

# +：打开用于更新（读取与写入）配合主模式使用
# r+ / w+ / x+ / a+
with open(file='a.txt', mode='w+', encoding='utf-8') as f:
    f.write('hello')
    # seek(offset, whence)方法：用于改变文件对象指针的位置
    # offset：偏移量，移动距离（注意：移动的是字节，不是字符；一个中文=3个字节）
    # whence：参考点：0 从文件开头计算（默认值） /  1 从当前位置计算  /  2 从文件末尾计算
    f.seek(0, 0)
    print(f.read())

with open(file='a.txt', mode='a+', encoding='utf-8') as f:
    f.write(' python')
    # seek(offset, whence)方法：用于改变文件对象指针的位置
    # offset：偏移量，移动距离（注意：移动的是字节，不是字符；一个中文=3个字节）
    # whence：参考点：0 从文件开头计算（默认值） /  1 从当前位置计算  /  2 从文件末尾计算
    f.seek(0, 0)
    print(f.read())