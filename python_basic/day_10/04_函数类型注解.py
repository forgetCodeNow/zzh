# 函数类型注解：给函数的参数和返回值添加类型注解
# 语法格式：def add(a: 类型) -> 返回值类型

def add(a: int, b: int) -> float:
    return a + b


# 设置返回值多个类型注解
def add1(l1: list[int]) -> set[float | int]:
    l2 = set(l1)
    return l2

# 设置*args参数类型
def add2(*args: int) -> float:
    return sum(args)

# 设置**kwargs的value值类型
def info(**kwargs: str | int):
    return kwargs

# 获取函数注解信息
print(add.__annotations__)  # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'float'>}