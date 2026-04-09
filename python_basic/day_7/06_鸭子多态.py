
# 没有继承
class Dog:
    # 没有方法重写
    def speak(self):
        print('dog speak')

class Cat:
    def speak(self):
        print('cat speak')

class Pig:
    def speak(self):
        print('pig speak')

def make_sound(animal):     # 不进行类型限制
    animal.speak()      # 多态的体现

d1 = Dog()
c1 = Cat()
p1 = Pig()
make_sound(d1)      # 同样可以调用Dog类的speak方法
make_sound(c1)      # 同样可以调用Cat类的speak方法
make_sound(p1)      # 同样可以调用Pig类的speak方法