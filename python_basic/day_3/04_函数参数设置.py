# 函数外部传参

def add(a, b):  # a ，b是形参， 接受外部传参的变量，仅可以在函数内部使用
    print(a + b)


# 从函数外部传参,传参要对应函数形参数量，不能少传
# 位置参数,使用位置参数时，不能跳过某个位置的参数，去给后面的形参赋值。
add(1, 2)

# 关键字参数，调用函数时，通过形参名=值的形式传递实参,函数会自动接受对应形参的值，不被位置影响，调用函数传参更明显易读
# 位置参数和关键字参数可以混用，注意：混用时位置参数必须在关键字参数前面
add(b=4, a=3)


# 错误写法，编译器报错,SyntaxError: positional argument follows keyword argument
# add(b=6,2)


# 限制传参方法 具体规则:/前边只能用位置参数，*后面只能用关键字参数。同时出现时，/必须在*前面
def add2(a, b, /, c, *, d):
    print(a + b + c + d)


add2(1, 2, c=3, d=4)


# 参数默认值，就是在定义函数时，直接给形参赋一个值;注意：默认值参数必须写在最后面
def add3(a, b, c= 3):
    print(a + b + c)

add3(1, 2)  # 可以不给形参传值，会使用默认值
add3(1, 2, 4)  # 也可以给形参传值，会覆盖默认值




# 可变位置参数，在定义函数形参中加上*，改形参就变成可变参数， 函数调用时，所有输入的位置实参都会被打包成元组，赋值给可变位置参数*args
def args_change_loc(*args):
    print(args)

args_change_loc(1,23,3,4,'dasd','hello')

# 可变关键之参数，在定义函数形参中加上**，改形参就变成可变参数， 函数调用时，所有输入的位置实参都会被打包成字典，赋值给可变位置参数**args

def args_change_keywords(**kwargs):
    print(kwargs)

args_change_keywords(a=1, b=2, c=3)

# 可变位置参数和可变位置参数一起使用，要求可变位置参数在可变关键字参数前面,同时也可以和其他参数一起使用，位置参数要在前面，可变关键字参数要在最后
def args_change(a, b, *args, c=-2, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

args_change(1,2,3,4,5,'hello',c=666,name='zhangsan',age=23)