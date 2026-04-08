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

    # 使用@staticmethod 修饰的方法就是静态方法，静态方法保存在类本身
    # 静态方法只是单纯定义在类中，不会收到self、cls参数，都是自定义参数
    # 因为不会收到self、cls参数，所有内部不会访问任何的类属性和实例属性
    # 静态方法的作用：用来写关于类的小工具
    @staticmethod
    def is_adult(bath_year):
        current_year = datetime.now().year
        age = current_year - bath_year
        return age >= 18

    @staticmethod
    def mask_idcrad(idcard):
        return idcard[:6] + '********' + idcard[-4:]


# 静态方法直接用类调用
result = Person.is_adult(2000)
print(result)
mask_idcard = Person.mask_idcrad('360730200103143819')
print(mask_idcard)



