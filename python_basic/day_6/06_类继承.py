class Person:

    def __init__(self, name, age):
        # 给实例添加属性
        self.name = name
        self.age = age

    # Person类的自定义方法
    def speak(self,msg):
        print(self.name,self.age,f'我想说{msg}')

class Student(Person):

    def __init__(self, name, age, stu_id, grade):
        # 继承父类__init__方法
        super().__init__(name, age)
        # Person.__init__(self, name, age)  这个也可以调用Person类的__init__初始化方法
        self.stu_id = stu_id
        self.grade = grade

# 创建Student实例对象
s1 = Student('zhangsan', 15, 260001, '初三')
print(s1.__dict__)

# 也可以继承父类的实例方法
s1.speak('hello')


