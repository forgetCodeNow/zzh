'''
函数·综合案例
需求:完成一个健身挑战赛程序。
1定义calc_total函数，用于统计总运动量(参数:多天的运动数据)。
2 定义calc_avg函数，用于统计平均运动量(参数:总运动量和天数)
3定义check success函数，用于反馈挑战是否成功(参数:总运动量和目标运动量)
4定义main函数，用于启动一场挑战赛(参数:比赛标题 和比赛持续天数)
'''

def  calc_total(days):
    total_sport = 0
    for i in range(1,days+1):
        total_sport += int(input(f'第{i}天，运动量是多少？'))
    print(f'你7天一共运动量是{total_sport}')
    return total_sport

def calc_avg(total_sport, days):
    print(f'你{days}天平均每天运动量大约是{int(total_sport/days)}')
    return total_sport/days

def check_success(total_sport, target_sport):
    if total_sport > target_sport:
        return True
    else:
        return False

def main(title, days):
    print(title)
    target_sport = 35
    return check_success(calc_avg(calc_total(days),days),target_sport)

result = main('7天俯卧撑挑战赛',7)
if result:
    print('恭喜你！挑战成功')
else:
    print('很遗憾，没有完成挑战目标')