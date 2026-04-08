from unittest import result


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

    # 在子类中定义和父类相同的方法，子类方法会覆盖掉父类的方法， 这就是方法重写
    def speak(self,msg):
        print(f'我是学生，学号{self.stu_id},年级{self.grade}')
        super().speak(msg)  # 也可以手动调用父类的方法


s1 = Student('zhangsan', 15, 260001, '初三')
s1.speak('hello')

# isinstance(instance, class) 判断某个实例对象是否是class类或class子类的实例对象
print(isinstance(s1,Person))
print(isinstance(s1,Student))
# issubclass(class1,class2) 判断class1类是否为class2类的子类
print(issubclass(Student,Person))
print(issubclass(Person,Student))