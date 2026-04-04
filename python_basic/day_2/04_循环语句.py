# while 基础语法
n = 1
while n <= 10:  # 条件判断语句
    print(f'hello, {n}!')
    n += 1
print(f'当前n的值：{n}')

'''
while循环案例
模拟一个密室逃脱场景
1用户必须正确的回答问题，才能“逃出密室”。
2若回答错误，系统就会不断循环提问，直到答对为止。
3若回答正确，控制台打印逃脱成功，并结束循环。
'''
print('==============密室逃脱案例=====================')
is_quit = False
while is_quit:
    num = int(input('3+3='))
    if num == 6:
        is_quit = False
        print('回答正确！逃脱成功！！！')
    else:
        is_quit = True
        print('回答错误，重新回答！')



# for 基础语法
name = 'zzh'
for n in range(0,10,2):
    print(n+1)
print(n)

for a in name:  # 字符串也可以作为可迭代对象
    print(a)

'''
for 循环案例
需求:设计一个字符串加密程序
使用ord() 和 chr()
'''
password_encrypt = ''
password = 'zzh123'
for i in password:
    i = ord(i)
    password_encrypt += chr(i+1)
print(f'加密前密码:{password}')
print(f'加密后密码:{password_encrypt}')


#嵌套循环，简单说就是循环里面套循环  循环嵌套越多，时间复杂度就越高，运行索要的时间就越久
for day in range(1,31):
    for i in range(4):
        print(f'第{day}天，第{i+1}次')

