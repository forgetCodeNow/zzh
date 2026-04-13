# 函数装饰器：
# 1、装饰器是一种【可调用对象】（通常是函数），可以接收一个函数作为参数，并返回一个函数
# 2、可以在不修改原函数代码的情况下，增强或改变原函数的功能
# 实际应用：在不改变原函数的前提下，给函数统一加上：日志，计时，校验，缓存，等功能

'''
关键点：
1、接收被修饰函数，同时返回新函数（wrapper）
2、修饰器返回的是wrapper函数，以后别人调用的也是用wrapper函数
3、为了保证参数的兼容性，wrapper函数要通过*args和**kwargs接收参数
4、wrapper函数中主要的作用是：调用原函数，执行其他逻辑，要把原函数返回出去
'''

# 修饰器：在原函数的基础上加了一个hello输出
def say_hello(func):
    def wrapper(*args,**kwargs):
        print('hello')
        return func(*args,**kwargs)
    return wrapper      # 必须返回wrapper函数

# 修饰器：在原函数的基础上加了一个bey输出
def say_bey(func):
    def wrapper(*args, **kwargs):
        res =  func(*args,**kwargs)
        print('bey')
        return res
    return wrapper


@say_hello
@say_bey
def add(a,b):
    res = a + b
    print(f'{a} + {b} = {a+b}')
    return res

result = add(1,2)

# 进阶的修饰器：带参数的修饰器
def outer(msg):
    def say_hello(func):
        def wrapper(*args, **kwargs):
            print(f'{msg}计算')
            print('hello')
            return func(*args, **kwargs)
        return wrapper  # 必须返回wrapper函数
    return say_hello

@outer('减法')        # 相当于传了’减法‘参数的say_hello修饰器，返回值是say_hello函数，里面有个参数
def sub(a,b):
    return a - b

sub(2,1)