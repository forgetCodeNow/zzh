class Person:

    def __init__(self, name, age, idcard):
        # 给实例添加属性
        self.name = name   # 共有属性
        self._age = age     # 受保护属性
        self.__idcard = idcard  # 私有属性

    # Person类的自定义方法
    def speak(self):
        print(self.name, self._age, self.__idcard)

class Student(Person):
    def hello(self):
        print(self.name, self._age, self.__idcard)


p1 = Person('zhangsan', 22, '0001')
# __idcard 属性被重命名为_Person__idcard,实现私有属性
print(p1.__dict__)  # 输出结果 {'name': 'zhangsan', '_age': 22, '_Person__idcard': '0001'}

print(p1._age)      # 受保护属性可以在类外部强制访问
print(p1.__idcard)      # 类外部访问私有属性 报错AttributeError: 'Person' object has no attribute '__idcard'

s1 = Student('zhangsan', 22, '0001')
s1.hello()      # 子类访问私有属性，报错 'Student' object has no attribute '_Student__idcard'