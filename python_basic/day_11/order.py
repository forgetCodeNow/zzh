max_amount = 10000000

def create_order():
    print("create order")

def cancel_order():
    print("cancel order")


def show_info():
    print("show info")

# 写了这个，在别的模块导入本模块时，不会执行函数调用
if __name__ == '__main__':
    create_order()
    cancel_order()