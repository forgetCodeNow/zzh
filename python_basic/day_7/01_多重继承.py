class Person:

    def __init__(self, name, age):
        # 给实例添加属性
        self.name = name
        self.age = age

    # Person类的自定义方法
    def speak(self):
        print(self.name,self.age)

class Worker:
    def __init__(self, company):
        self.company = company

    def do_work(self):
        print(f'我在{self.company}兼职')

class Student(Worker, Person):
    def __init__(self, name, age, company, stu_id, grade):
        # super().__init__(name, age)  # 如果只能super（），那么只会初始化Student类继承的第一个类Person，Worker类无法初始化
        Person.__init__(self, name, age)  # 使用类.__init__() 初始化父类实例属性
        Worker.__init__(self, company)
        self.stu_id = stu_id
        self.grade = grade

    def study(self):
        print(f'我在{self.grade}学习')

# 初始化实例对象
s1 = Student('张三', 22, 'KFC', '0001', '初三')
print(s1.__dict__)

# 实例对象调用父类方法
s1.speak()
s1.do_work()
s1.study()


# __mro__ 属性：可以记录属性和方法的查找顺序
print(Student.__mro__)
