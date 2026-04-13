# 类装饰器
# 1、包含__call__ 方法的类，就是类装饰器
# 2、调用函数方法一样调用类装饰器的实例对象，就会触发__call__方法
# 3、__call__方法通常接收一个函数作为参数，并返回一个函数

class SayHello:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('hello')
            return func(*args, **kwargs)
        return wrapper

class SayBey:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            res =  func(*args, **kwargs)
            print('bey')
            return res
        return wrapper

# 类装饰器必须带()，相当于实例化类
@SayHello()
@SayBey()
def add(a, b):
    print(f'{a} + {b} = {a+b}')
    return a + b

result = add(1, 2)

# 带参数的就加一个__init__初始化方法加上参数