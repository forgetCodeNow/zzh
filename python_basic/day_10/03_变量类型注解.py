# 变量类型注解：就是定义变量的类型
# 不可变对象
a: int | str = 10   # int / str类型
b: float = 1.2
c: str = '123'
d: bool = True

# 注意：可以先写变量的类型注解，以后再赋值，这个变量不会被创建
str1: str

# 可变对象
# 列表 集合 字典
eat: list[str | int] = [1, 2, 3]    # int / str类型
stu: set[str | int] = {1, 2, 3}     # int / str类型
names: dict[str | int, int] = {'zhangdan': 22, 22: 30}      # key:int / str  value:int

# 特殊：元组
t1: tuple[int] = (2,)   # 写几个类型就只能有几个元素
# 多元素类型
t2: tuple[int, ...] = (1, 2, 3)     # 可以有多个int类型的元素