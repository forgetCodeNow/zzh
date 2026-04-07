# 字典key不能重复，重复出现后面的会覆盖前面的
d1 = {'name': 'zhangsan', 'age': 22, 'name': 'lisi'}
print(d1)  # 输出结果{'name': 'lisi', 'age': 22}

# 定义空字典
d2 = {}
d3 = dict()
print(d2, d3)

# 字典的key必须是不可变类型，value可以是任意类型
d4 = {('eat', 'drink'): 'action'}  # 可以执行，因为元组是不可变的
# d5 = {['eat', 'drink']:'action'}  # 报错，列表是可变容器，不能做key

# 字典可以嵌套
stu_dict = {202604001: {'name': 'zhangsan', 'age': 22, 'class': 'gaosan'}}
print(stu_dict)
