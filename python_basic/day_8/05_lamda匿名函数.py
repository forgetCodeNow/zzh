# 使用场景：当一个函数只用一次，只做一点点事，使用匿名函数更简洁
'''
注意点：
1、代码只能写一行
2、不能写代码块（if，while for）
3、冒号后面必须时表达式，且只能有一个表达式，可以是条件表达式
4、表达式结果自动作为返回值
'''

def calculate(func, a, b):
    print(func(a, b))
result = lambda x, y : x + y
calculate(result, 1, 2)

calculate(lambda x, y : x + y, 3, 2)


result2 = lambda age : '成年' if age >= 18 else '未成年'
print(result2(19))
print(result2(11))