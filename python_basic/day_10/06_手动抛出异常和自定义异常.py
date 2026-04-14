# 手动抛出异常：raise 异常类型（）
try:
    age = int(input('请输入年龄'))
    if age >= 18:
        print('年成人')
    elif 0 < age < 18:
        print('未成年人')
    else:
        print('输入错误')
        # 手动抛出异常
        raise ValueError('输入有误')
except Exception as e:
    print(e)


# 异常传递机制
# 1、如果异常没有被当前代码块捕获处理，那该异常就会沿着调用链，逐层传递给调用者
# 2、如果所有调用者都没有捕获处理异常，那程序最终会因异常未处理终止

def test1():
    print('join test1')
    print(x)        # NameError异常，外层没有异常处理，程序直接终止，后续代码不再执行
    print('quit test1')

def test2():
    print('join test2')
    try:        # 在这里捕获异常，test1出现异常后面的代码都不执行，直接传递给test2
        test1()
    except Exception as e:
        print(e)
    print('quit test2')

def test3():
    print('join test3')
    test2()
    print('quit test3')

test3()


# 自定义异常
# 1、必须继承Except异常类
class IdLenError(Exception):
    # msg接收异常传递参数
    def __init__(self,msg):
        super().__init__('【身份证长度异常】'+msg)

# 手动抛出异常
raise IdLenError('身份证长度错误')