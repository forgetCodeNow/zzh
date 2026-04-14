# __init__文件是包的初始化文件，包被导入时会自动调用
# 可以编写包的初始化逻辑
# 所定义的内容，会被from 包 import * 形式全部引入
# 一样可以用__all__来控制from 包 import * 引入

print('trade包的初始化')