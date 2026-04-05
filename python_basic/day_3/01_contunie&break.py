for n in range(1, 10):
    if n % 2 == 0:  # 只打印奇数
        continue  # 跳过本次循环，进入下一次循环
    print(n)

for i in range(1, 10):
    if i == 6:  # 只打印小于6的数
        break  # 直接跳出循环体
    print(i)
