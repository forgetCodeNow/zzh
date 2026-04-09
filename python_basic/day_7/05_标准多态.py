class Animal:
    def speak(self):
        print('animal speak')

class Dog(Animal):
    def speak(self):
        print('dog speak')

class Cat(Animal):
    def speak(self):
        print('cat speak')

class Pig:
    def speak(self):
        print('pig speak')

def make_sound(animal: Animal):     # 类型注解
    animal.speak()      # 多态的体现

a1 = Animal()
d1 = Dog()
c1 = Cat()
p1 = Pig()
make_sound(a1)
make_sound(d1)      # 调用的是Dog类的speak方法
make_sound(c1)      # 调用的是Cat类的speak方法
make_sound(p1)      # 能调用Pig方法，但是不推荐这样写，没有继承Animal类