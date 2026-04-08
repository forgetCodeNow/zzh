from datetime import datetime

class Person:
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

    # 类方法,使用@classmethod 修饰器的就是类方法
    # 类方法的形参为，类本身和自定义参数
    # 类方法中可以访问类属性
    # 类方法的作用：实现与类有关的逻辑，如：操作类级别信息、实现工厂方法
    @classmethod  # 修饰器，表示下面写的方法是类方法
    def change_panet(cls, planet):
        cls.planet = planet  # 这里修改的是类属性，调用次方法后，所有的实例对象访问planet类属性都被更改

    # 通过特定类型信息创建实例对象
    @classmethod
    def create(cls, info_str):  # info_str = 'lsi-2001'
        name, year =  info_str.split('-')
        age = datetime.now().year - int(year)
        return cls(name, age)


# 创建实例对象
p1 = Person('zhangsan', 22)
p2 = Person.create('lisi-2001')
print(p1.__dict__)
print(p2.__dict__)
print(p1.planet)

# 通过类方法修改类属性，修改后所有的实例对象访问类属性都会变
Person.change_panet('美国')
p3 = Person.create('wangwu-1999')
print(p3.planet)
print(p1.planet)
print(p2.planet)



