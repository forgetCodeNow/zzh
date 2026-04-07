'''
#练习一:水果清单
#需求1:打印所有的水果
#需求2:找到最贵水果
'''
from itertools import count

fruits = {
    'apple': 4.5,
    'banana': 3.5,
    'orange': 9.9
}
# 打印水果清单
print(tuple(fruits.items()))

# 找到最贵的水果
most_expensive = 0
most_expensive_fruit = None
for key in fruits:
    if fruits[key] > most_expensive:
        most_expensive = fruits[key]
        most_expensive_fruit = key
print(most_expensive_fruit)

# 字典使用max()函数
# 对比value值，返回对应的key
print(max(fruits, key=fruits.get))

'''
#练习二:学生成绩表
#需求1:计算每位学生的平均分
#需求2:找到总分最高的学生
'''
print('#练习二:学生成绩表==================================================')

stu = [{
    'name': 'zhangsan',
    'score': {'语文': 66, '数学': 99, '英语': 25}
},
    {
        'name': 'lisi',
        'score': {'语文': 60, '数学': 78, '英语': 88}
    },
    {
        'name': 'wangwu',
        'score': {'语文': 55, '数学': 23, '英语': 34}
    }
]

# 需求1:计算每位学生的平均分
for student in stu:
    score = (student.get('score'))
    sum_score = sum(tuple(score.values()))
    avg_score = sum_score / len(student.get('score').keys())
    print(f'{student.get('name')}的平均成绩{avg_score:.2f}')
    student.update({'avg_score': round(avg_score, 2)})

#需求2:找到总分最高的学生
best_student = []
best_score = 0
for student in stu:
    sum_score = sum(student.get('score').values())
    if sum_score > best_score:
        best_score = sum_score
        best_student = student.get('name')
    elif sum_score == best_score:
        best_student.append(student.get('name'))

print(f'最高分{best_score},最高分学生{best_student}')



print('练习三:评论内容====================================')
'''
练习三:评论内容
#comment='这家奶茶真好喝，环境也不错，就是价格有点贵，好喝好喝好喝!强烈推荐!
#需求1:统计“好喝”出现次数
#需求2:将字符串中的“贵”替换为“略高”
#需求3:是否包含“推荐”两个字
'''

comment='这家奶茶真好喝，环境也不错，就是价格有点贵，好喝好喝好喝!强烈推荐!'
#需求1:统计“好喝”出现次数
print(f'好喝出现{comment.count('好喝')}次')
#需求2:将字符串中的“贵”替换为“略高”
comment = comment.replace('贵', '略高')
print(comment)
#需求3:是否包含“推荐”两个字
result = '推荐' in comment
print(result)