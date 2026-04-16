# with主要用于管理程序中需要成对出现的操作
# （上错 解锁）（打开 关闭）（借用 归还）

# 2、目标就是让程序自动处理进入和离开的操作，我们只需要写业务逻辑

# 3、语法格式、
# with 能得到上下文管理器的表达式 as 变量:
#     代码体

# 4、上下文管理器协议
# __enter__()方法，在进入with之前会自动调用__enter__()方法
# __exit__()方法，在离开with之前会自动调用，无论代码体是否异常都会调用

# 实现上下文管理器
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __enter__(self):
        print('进入with之前的逻辑')
        # 调用__enter__()方法会有一个返回值
        return self

    # 返回True时说明异常已处理，不在抛出异常
    # 返回False时说明异常没有被处理，会抛出异常
    def __exit__(self, type, value, traceback):
        print('离开with之前的逻辑')
        # type：异常类型
        # value：异常对象
        # traceback：异常追踪信息
        if type:
            print(type)
            print(value)
            print(traceback)
        return True

    def test(self):
        print('test')

with Person('zhangsan', 22) as p1:
    p1.test()
    p1.a()      # p1没有a()方法，并且__exit__()方法返回值是False，抛出异常
    # 异常后面的代码不执行，但是exit还是会执行
    print('error')

