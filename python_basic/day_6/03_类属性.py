class Person:
    # max_age、planet 都是Person类的类属性,保存在类自身上
    # 类属性可以通过类访问，也可以通过实例访问
    # 类属性一般放‘公共数据‘
    max_age = 120
    planet = '中国'

    def __init__(self, name, age):
        # 给实例添加属性
        self.name = name
        # 使用类属性约束实例对象的创建
        if age <= Person.max_age:
            self.age = age
        else:
            self.age = Person.max_age

p1 = Person('zhangsan', 18)
print(Person.max_age)
print(p1.max_age)

# 相当于p1实例创建了一个planet的实例属性，覆盖了Person的类属性，用p1实例访问planet只会访问到实例属性
p1.planet = '美国 '
print(p1.__dict__)  # 返回结果 {'name': 'zhangsan', 'age': 18, 'planet': '美国 '}

# 验证age实例属性约束
p2 = Person('lisi', 190)
print(p2.__dict__)  # 返回结果 {'name': 'lisi', 'age': 120}