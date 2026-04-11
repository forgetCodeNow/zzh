# 1、函数返回多值
def compute(a, b):
    return a + b, a * b


result = compute(1, 2)  # 将多返回值打包成元组
print(result)
r1, r2 = compute(1, 2)  # 使用多变量接收多返回值
print(r1, r2)


# 2、函数打包接收参数
# *args 接收位置参数打包成元组
# **kwargs 接收关键字参数打包成字典
def test1(*args, **kwargs):
    print(args)
    print(kwargs)


test1(1, 2, 3, 4, 'hello', name='world', age=20)


# 3、函数解包传递参数
s1 = (1,2)
d1 = {'name': 'world', 'age': 20 }
def test2(a, b, name, age):
    print(a, b, name, age)

# *s1 将s1元组解包成一个个元素
# **d1 将d1字典解包成一个个item
test2(*s1,**d1)
