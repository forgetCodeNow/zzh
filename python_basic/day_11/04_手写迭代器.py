'''
前提：
可迭代对象要可以使用__iter__()方法
可以使用__iter__()和__next__()方法的就是迭代器
'''

# 实现方法一
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __iter__(self):
        # __iter__()方法返回迭代器
        return PersonIteration(self)

# 自定义手写迭代器
class PersonIteration:
    def __init__(self, person):
        self.person = person
        # 迭代器指针
        self.index = 0
        # 迭代器容器
        self.attrs = [person.name, person.age]

    # 可以使用__iter__()和__next__()方法的就是迭代器
    def __iter__(self):
        return self

    # 调用指针取出元素
    def __next__(self):
        # 迭代器元素取完后手动抛出StopIteration 异常
        if self.index >= len(self.attrs):
            raise StopIteration
        result = self.attrs[self.index]
        self.index += 1
        return result

p1 = Person('zhangsan', 22)
for item in p1:
    print(item)
for item in p1:
    print(item)
for item in p1:
    print(item)

print('实现方法二' * 3)
# 实现方法二，不使用手写迭代器类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.index = 0
        self.attrs = [name, age]

    def __iter__(self):
        # 每次调用iter(Person)重置指针位置，避免了只能调用一次问题
        self.index = 0
        # __iter__()方法返回迭代器
        return self

    def __next__(self):
        if self.index >= len(self.attrs):
            raise StopIteration
        result = self.attrs[self.index]
        self.index += 1
        return result

p1 = Person('zhangsan', 22)
for item in p1:
    print(item)
for item in p1:
    print(item)
for item in p1:
    print(item)