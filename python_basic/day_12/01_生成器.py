# 1、生成器
# 生成器函数：函数体中出现yield关键字，那么这个函数就是生成器函数
# 生成器对象：调用函数时，函数体不会立刻执行，会返回一个生成器对象
# 生成器对象调用next()方法才会执行函数体函数，遇到yield会暂停执行，并返回yield后面的表达式结果，同时记录当前yield位置
# 遇到return是会抛出StopIteration异常，并将return后面的表达式，作为异常信息

def demo():
    print('demo top')
    yield       # yield 后面可以跟表达式，生成器对象每次next()返回的就是这个表达式的结果，不写默认None
    print('demo middle')
    yield '这是demo middle 和 bottom 中间'
    print('demo bottom')
    return 1

d1 = demo()
for item in d1:
    print(item)


# 2、生成器对象时一种特殊的迭代器（本质是通过yield自动实现了迭代器协议）
d2 = demo()
print(iter(d2) == d2)       # True 表示iter(d2)返回的迭代器和d2是一样的，符合迭代器iter(迭代器)返回自身协议
for item in d2:     # iter(d2) -> next(d2)
    print(item)

# 3、yield也能写在循环里
def cars(total):
    for i in range(1,total+1):
        yield f'第{i}台车'
cars = cars(10)
for item in cars:
    # print(item)
    pass


# 3、yield from 能把一个可迭代对象里的东西依次yield出去，可以代替 for + yield
def demo2():
    nums = [1,2,3,4]
    yield from nums

d3  = demo2()
for item in d3:
    # print(item)
    pass

# 4、使用生成器对象.send()，可以让生成器继承执行的同时，给上一次yield传值
# 第一次启动生成器，不能传值
def demo():
    print('demo top')
    x = yield '这是demo top 和 middle 中间'
    print(x)
    print('demo middle')
    y = yield '这是demo middle 和 bottom 中间'
    print(y)
    print('demo bottom')
    return 1

d4 = demo()
next(d4)
d4.send('x = 10')
try:
    d4.send('y = 20')
except StopIteration as e:
    print(e)


# 使用生成器遍历Person类实例对象
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__attr = [name, age]

    def __iter__(self):         # 变成了生成器函数
        # __iter__()方法返回迭代器
        yield from self.__attr


p1 = Person('zhangsan', 22)
for item in p1:     # 调用iter(p1)，返回一个生成器对象
    print(item)


# 使用生成器实现斐波那契数列
def fibo(total):
    pre = 1
    cur = 1

    for index in range(total):
        if index < 2:
            yield 1
        else:
            vlaue = pre + cur
            pre, cur = cur, vlaue
            yield vlaue

f1 = fibo(10)
for num in f1:
    print(num)


# 生成器表达式：(表达式 for 变量 in 可迭代对象)
# 返回的是一个生成器对象
# 什么时候使用生成器表达式：当每个结果，只依赖当前一个元素时
nums = (n for n in range(10))
print(nums)     # <generator object <genexpr> at 0x0000024812D21CC0> nums是一个生成器对象