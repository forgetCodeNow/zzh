'''
列表(list)·小练习
需求:实现一个成绩统计程序，可以对多名学生的成绩，进行统计和分析。
备注:用户可以连续输入学生成绩，直到用户输入"结束”字符串。
求：
总人数
最高分
最低分
合格人数：分数大于等于60
合格率
优秀人数：分数大于等于90
优秀率
平均分
'''

def stu_total(stu_score_list):
    return len(stu_score_list)

def max_score(stu_score_list):
    return max(stu_score_list)

def min_score(stu_score_list):
    return min(stu_score_list)

def avg_score(stu_score_list):
    return sum(stu_score_list) / len(stu_score_list)

def qua_num(stu_score_list):
    qua_num = 0
    for item in stu_score_list:
        if item >= 60:
            qua_num += 1
    return qua_num, qua_num / len(stu_score_list)

def exc_num(stu_score_list):
    exc_num = 0
    for item in stu_score_list:
        if item >= 90:
            exc_num += 1
    return exc_num, exc_num / len(stu_score_list)

stu_score_list = []
while True:
    score = input('请输入学生成，完成后输入结束：')
    if score == '结束':
        break
    stu_score_list.append(int(score))

if stu_total(stu_score_list) == 0:
    print('没有输入成绩')
    exit()
print(f'总人数：{stu_total(stu_score_list)}')
print(f'最高分：{max_score(stu_score_list)}')
print(f'最低分：{min_score(stu_score_list)}')
qua_num, qua_rate = qua_num(stu_score_list)
print(f'合格人数：{qua_num} ， 合格率：{qua_rate:.2%}')
exc_num, exc_rate = exc_num(stu_score_list)
print(f'优秀人数：{exc_num} ， 优秀率：{exc_rate:.2%}')
print(f'平均分：{avg_score(stu_score_list):.2f}')
