# 分支 基于判断结果，来决定走那条路

name = input('your name: ')
age = int(input('your age: '))

# 单分支
if age >= 18:  # 逻辑判断，只有True和False两种结果
    print('you are a adult')

# 双分支
if age >= 18:
    print('you are a adult')
else:
    print('you are a teen')

# 多分支
# 区分不同年龄段 1-10:baby 11-17:teen 18-60:adult >60:older
if 1 <= age <= 10:
    print('you are a baby')
elif age <= 18:
    print('you are a teen')
elif age <= 60:
    print('you are a adult')
elif age > 60:
    print('you are a older')

# 嵌套循环  ,简单说就是if里面套if|
if age < 18:
    if age < 10:
        print('you are a baby')
    else:
        print('you are a teen')
elif age >= 18:
    if age < 60:
        print('you are a adult')
    else:
        print('you are a older')

'''
为长跑俱乐部，设计一个马拉松比赛报名审核程序，具体规则如下:
1参赛年龄必须是:18~45岁之间。
2参赛前必须提交体检报告，否则不能比赛。
3比赛结束后，根据会员的等级，领取不同礼物:
1级会员礼物为:纪念T恤1
2级会员礼物为:专业跑鞋
3级会员礼物为:运动耳机
'''
if 18 <= age <= 45:
    is_report = int(input('是否有体检报告(0是无，1是有):'))  # 注意：input输入默认是字符串
    if is_report:
        print(f'恭喜你{name}！报名成功')
        vip_level = int(input('your vip level: '))
        if vip_level == 1:
            print(f'恭喜你{name}！获得纪念T恤1')
        elif vip_level == 2:
            print(f'恭喜你{name}！专业跑鞋')
        elif vip_level == 3:
            print(f'恭喜你{name}！运动耳机')
        else:
            print('您还不是会员')
    else:
        print('很遗憾，您不符合报名条件')
else:
    print('很遗憾，您不符合报名条件')
