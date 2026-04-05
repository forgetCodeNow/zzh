def add(a, b):
    print(a + b)

result = add(1, 2)  # 函数没有设置返回值时，默认返回None
print(type(result))  #返回值时NoneType类型

def add2(a, b):
    return a + b    # 结束函数执行

result2 = add2(3, 4)  # 接收函数执行结束后的return返回值
print(result2)
