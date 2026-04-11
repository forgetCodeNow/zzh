# 1、函数也是对象
from zlib import adler32

a1= 100             # int类的实例对象
a2 = 'hello'        # str类的实例对象
a3 = [1,2,3]        # list类的实例对象

def hello():        # hello函数是function类的实例对象
    print('hello')

print(type(a1))
print(type(a2))
print(type(a3))
print(type(hello))      # <class 'function'>

# 2、函数可以动态添加属性
def hello():
    print('hello')

hello.name = 'hello_one'    # 在函数中添加属性
print(hello.name)       # hello_one

# 3、函数可以复制给变量
def hello():
    print('hello')

h = hello
h()

# 4、可变参数 VS 不可变参数
# 不可变参数,函数内部改变不会影响外部不可变参数
# 主要看内存变化
a_int = 10
def change(a):
    print(a)
    a = 20
    print(a)
print(a_int)
change(a_int)
print(a_int)

# 可变参数,函数内部的改变会作用到外部可变参数
# 主要看内存变化，a_list list 都指向同一个内存地址（这个内存地址存的是元素的内存地址），并不直接指向列表中元素的内存地址
a_list = [1,2,3,4,5]
def change_list(list):
    print(f'list内存地址{id(list)}',list)
    list[0] = 6
    print(f'list内存地址{id(list)}',list)
print(f'a_list内存地址{id(a_list)}',a_list)
change_list(a_list)
print(f'a_list内存地址{id(a_list)}',a_list)

# 5、函数也可以作为参数
def hello(f):
    print('hello')
    f()

def bey():
    print('bey')
hello(bey)      # 注意：传入函数参数不带()，带()是调用函数

# 6、函数也可以作为返回值
def hello():
    print('hello')
    def bey(b):
        print(b+b)
    return bey
b1 = hello()    # b1 = bey函数
b1('bey')
# 第二种用法
print('第二种用法====')
hello()('bey')