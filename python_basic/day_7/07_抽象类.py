from abc import ABC, abstractmethod

# 定义抽象类必须继承ABC类
class Animal(ABC):
    # 定义抽象方法
    @abstractmethod
    def birth(self):
        pass

    def speak(self):
        print(f'{self.name} speak')

class Dog(Animal):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def birth(self):
        print(f'{self.name} birth')

d1 = Dog('David', 'female')
d1.speak()
d1.birth()