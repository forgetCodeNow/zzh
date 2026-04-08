class Person:
    # __init__(self) 初始化方法，在实例化对象时会自动给调用该方法
    # __init__(self) 主要作用：给正在创建的实例对象添加属性

    def __init__(self, name, age):
        # 给实例添加属性
        self.name = name
        self.age = age

    # Person类的自定义方法
    def speak(self,msg):
        print(self.name,self.age,f'我想说{msg}')


p1 = Person('zhangsan', 23)

# speak() 自定义方法执行过程，第一步会先在p1实例对象自身查找speak方法，如果没有找到，
# 第二步到实例对象的原始类里面去查找speak方法调用
p1.speak('hello')

def speak():
    print('outside speak')

# 把函数speak给到p1作为speak方法，这时执行p1.speak方法调用的就是外部speak函数
p1.speak = speak
print(p1.__dict__)  # 输出结果，存在speak方法：{'name': 'zhangsan', 'age': 23, 'speak': <function speak at 0x00000241898176A0>}
p1.speak()  # 输出结果：outside speak