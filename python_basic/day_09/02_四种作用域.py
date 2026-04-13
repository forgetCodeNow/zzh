# 全局作用域
a = 100
def test():         # 外层函数作用域
    global a        # 声明全局变量a
    a = 200
    b = 300
    print('test:',a)
    print('test:',b)

    def innner():       # 局部作用域
        nonlocal b      # 继承外层函数变量
        b = 400
        print('innner:',b)