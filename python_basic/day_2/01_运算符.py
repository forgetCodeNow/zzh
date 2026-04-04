a = 2
b = 3
c = '6'
d = 1.1

# 算数运算符 + - * / // % **
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # 除法默认返回结果是浮点型
print(a // b)
print(a % b)
print(a ** b)  # 指数 = a 的 b次方

# 比较运算符 == != > < <= >=
print(a == b)  # ==必须是相同的类型
print(a != b)
print(a > d)  # > < 必须是相同类型，但是整形和浮点型是可以做比较的
print(a < b)
print(a >= b)
print(a <= b)

print('字符串类型转换==============================')
# 字符串比较,python会先把字符串每个字符转成Unicode对应编码，在进行比较，ord()可以查看单个字符的Unicode编码,chr()可以把Unicode编码转换成字符
abc = 'abc'
abcd = 'abcd'
print(ord('a'))
print(ord('我'))
print(chr(97))
print(abc > abcd)  # 结果是False，先比较‘abc’的Unicode编码，编码相等，且字符到最后一位了，直接比较字符串长度

print('bool类型转换==============================')
# bool类型，bool类型转换时，数值除了0钻换成False，其他都转换成true；字符串转换时，除了空值，其他字符串都转换成True
print(bool(1999))
print(bool(1))
print(bool(0))
print((bool(3.14e10)))

print(bool(None))
print(bool('你是真是假'))
print(bool('False'))  # 结果为True

print('逻辑运算符================================')
# 逻辑运算符 and or not
# and 用于判断两边值是否都为True,and 还具备逻辑短路功能， 如果前面的值为False，则直接跳出判断不会执行后面的值
# and 运行规则：从左往右执行，如果左边是False,就直接返回左边，否则返回右边
print(True and True)
print(True and False)

print(3 - 3 and 4)  # 左边是False,结果返回0
print(3 + 3 and 4)  # 左边是True,返回结果是4

# or 用于判断两边是否至少有一个True,or 也具备逻辑短路能力，左右为True时，右边不执行
# or 运行规则：从左往右执行，如果左边是True,就直接返回左边，否则返回右边
print(True or False)
print(False or True)

print(3 - 3 or 4)  # 左边是False,结果返回4
print(3 + 3 or 4)  # 左边是True,返回结果是6
print(3 - 3 or 0)  # 左边是False,结果返回0

# not 用于取反,not返回值一定是bool值
print(not True)
print(not False)
print(not 3-3)
print(not 3 or not 4)   # 结果为False，两边都取反，两边都是False，or返回False
