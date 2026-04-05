# 简单说就是在函数中调用其他函数

def test1():
    print('begin test1')
    test2()  # test1（）函数中调用test2（）函数
    print('end test1')


def test2():
    print('begin test2')
    print('end test2')


test1()

# 函数嵌套使用可以实现函数递归效果
'''
实现1+2+3+4+5+6+7+8+9+10+11+12....
'''


def recursion(num):
    if num > 1:
        num += recursion(num - 1)
    else:
        return num
    return num


num = recursion(5)
print(num)

'''
实现1*2*3*4*5*6*7*8.....
'''


def recursion2(num):
    if num > 1:
        num *= recursion(num - 1)
    else:
        return num
    return num


num2 = recursion2(10)
print(num2)
