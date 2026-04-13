'''
try:
    可能会出现异常的代码块
except:
    出现异常后会执行的代码
else:
    没有出现异常会执行的代码
finally:
    不管有没有异常都会执行的代码
'''


try:
    num1 = int(input('请输入第一个数：'))
    num2 = int(input('请输入第二个数：'))
    res = num1 / num2
# 可以捕获不同的异常
except (ValueError, TypeError, NameError, ZeroDivisionError, Exception) as e:
    if isinstance(e, ZeroDivisionError):
        print('0不能作为除数')
    elif isinstance(e, ValueError):
        print('必须输入数字')
    else:
        print('异常')
else:
    print('代码执行无异常')
finally:
    print('有没有异常都辛苦了!')
