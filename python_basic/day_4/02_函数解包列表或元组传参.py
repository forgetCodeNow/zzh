def test(data):
    print(data)

def test2(*data):   # *data会把所接收到的元素打包成一个元组
    print(data)

list1 = [1, 2, 3]
t1 = ('1', '2', '3')

# 正常传参
test(list1)
test(t1)

# 解包传参
'''
相当于把列表list1中的元素解包出来，
变所有会报成三个参数传给test（）函数，
但是test（）只有一个形参，
所以会报错test() takes 1 positional argument but 3 were given
'''
# test(*list1)

# 可以把解包参数传给带可变形参的函数
test2(*list1)
test2(*t1)

