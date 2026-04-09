
class Person:
    def __init__(self, name, age, idcard):
        # 给实例添加属性
        self.name = name   # 共有属性
        self._age = age     # 受保护属性
        self.__idcard = idcard  # 私有属性

    # 注册age 的getter方法，当访问Person类的age属性时，下面的age方法就会自动调用
    @property
    def age(self):
        return self._age

    # 注册age 的setter方法，当修改Person类的age属性时，下面的age方法就会自动调用
    @age.setter
    def age(self, value):
        self._age = value

    # 注册idcard 的getter方法，当访问Person类的idcard属性时，下面的idcard方法就会自动调用
    @property
    def idcard(self):
        # 可以在里面加限制，判断账户是否正常才给看
        return self.__idcard

    # 注册idcard 的setter方法，当修改Person类的idcard属性时，下面的idcard方法就会自动调用
    @idcard.setter
    def idcard(self, value):
        # 可以在里面加限制
        print('身份证不让修改！')


p1 = Person('张三', 22, '000001')
print(p1.name)

# 如何安全访问受保护属性
print(p1.age)
p1.age = 66
print(p1.age)

# 如何安全访问私有属性
print(p1.idcard)
p1.idcard = '00012'