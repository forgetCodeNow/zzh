import main
import order
import pay

order.create_order()
pay.ali_pay()

# 给模块设置别名
import order as od

# 从模块引入单独的方法/变量
from order import create_order, cancel_order

# 给引入多个方法设置别名，避免同名方法冲突
from pay import wechat_pay as wpay, ali_pay as apay, show_info
from order import show_info

# 这个调用的是order的show_info，pay的show_info被后引入的覆盖了
show_info()

# 关于__all__
# 在Python模块中。可以通过__all__来控制from 模块 import * 导入的模块
# __all__ 的值可以是元组和列表，里面的元素是字符串

# 关于__name__
# 是每个.py文件的内置变量
# 1、作为主程序运行时值是__main__
# 2、作为模块导入时值是模块文件名
# 作用：防止模块引入时产生影响

if __name__ == '__main__':
    show_info()


