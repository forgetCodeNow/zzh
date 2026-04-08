# 定义一个Person类（类名一般使用大驼峰写法）

class Person:
    # __init__(self) 初始化方法，在实例化对象时会自动给调用该方法
    # __init__(self) 主要作用：给正在创建的实例对象添加属性

    def __init__(self, name, age):
        # 给实例添加属性
        self.name = name
        self.age = age

# 创建一个对象
p1 = Person('zhangsan', 33)

# 访问对象的属性
print(p1.name)
print(p1.age)

# 对象.__dict__方法可以直接查看对象的所有属性
print(p1.__dict__)

# 对象.属性名 = 值 可以添加对象属性
p1.weight = 80
print(p1.__dict__)

# type()方法可以查看对象属于哪个类
print(type(p1))
