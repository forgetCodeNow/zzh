
class Person:
    # __init__魔法方法，在创建Person类时调用
    def __init__(self, name, age):
        # 给实例添加属性
        self.name = name   # 共有属性
        self.age = age     # 受保护属性

    # 执行print(Person实例对象） / str(Person实例对象) 时调用
    def __str__(self):
        # return self.__dict__      # 返回值必须时string类型
        return f'{self.name}-{self.age}'

    # 执行len（实例对象）时调用
    def __len__(self):
        return len(self.__dict__)

    # 执行实例对象1 < 实例对象2 时调用
    def __lt__(self, other):
        return self.age < other.age

    # 执行实例对象1 > 实例对象2 时调用
    def __gt__(self, other):
        return self.age > other.age

    # 执行实例对象1 == 实例对象2 时调用
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # 当访问不存在属性时调用
    def __getattr__(self, item):
        return '这个属性不存在'


p1 = Person('zhangsan', 18)
p2 = Person('lisi', 18)
print(p1)   # 调用__str__
print(p2)   # 调用__str__
print(len(p1))  # 调用__len__
print(len(p2))  # 调用__len__
print(p1 < p2)  # 调用__lt__
print(p1 > p2)  # 调用__gt__
print(p1 == p2) # 调用__eq__
print(p1.idcard)    # 调用__getattr__