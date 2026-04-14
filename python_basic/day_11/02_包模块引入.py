# 给模块设置别名
import trade
import trade.order as od

# 从模块引入单独的方法/变量
from trade.order import create_order, cancel_order

# 给引入多个方法设置别名，避免同名方法冲突
from trade.pay import wechat_pay as wpay, ali_pay as apay, show_info as pay_show
from trade.order import show_info as order_show

# 包的特殊导入
from trade import pay
from trade import order as od
from trade import *

# 引入子包（包中包）
# from 包名.子包名 import 模块名


if __name__ == '__main__':
    trade.order.create_order()
    wpay()
    order_show()
    pay_show()