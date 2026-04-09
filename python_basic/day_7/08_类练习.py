'''
***************学生管理***************
1.添加学生
2.删除学生
3.查看所有学生
4.录入成绩
5.退出
请输入操作序号
'''

from datetime import datetime

class Person:
    def __init__(self, name, age, gender, idcard):
        self.name = name
        self.age = age
        self.gender = gender
        self.idcard = idcard

class Student(Person):
    count = 0

    def __init__(self, name, age, gender, idcard):
        super().__init__(name, age, gender, idcard)
        Student.count += 1
        self.stu_id = f'{datetime.now().year}{Student.count:03d}'
        self.scores = {}

    # 给当前学生添加成绩
    def add_score(self, subject, score):
        self.scores[subject] = score

    def __str__(self):
        return f'{self.name}-{self.age}-{self.gender}-{self.idcard}-{self.stu_id}-{self.scores}'

class Magener:
    def __init__(self):
        self.student_data = list()

    # 添加学生信息
    def add_student(self):
        name = input('请输入姓名')
        age = int(input('请输出年龄'))
        gender = input('请输出性别')
        idcard = input('请输出身份证号')
        stu = Student(name, age, gender, idcard)
        self.student_data.append(stu)
        print(f'添加成功，学号是{stu.stu_id}')

    # 删除学生信息
    def del_student(self):
        stu_id = input('请输出删除学生的学号')
        target = None
        for stu in self.student_data:
            if stu.stu_id == stu_id:
                print(f'删除{stu.name}学生成功')
                target = stu
                break
        if target is None:
            print('学号有误')
        else:
            self.student_data.remove(target)

    # 打印所有学生成绩
    def print_all_student(self):
        for student in self.student_data:
            print(student.__dict__)

    # 添加学生成绩
    def input_score(self):
        stu_id = input('请输出学生的学号')
        for stu in self.student_data:
            if stu.stu_id == stu_id:
                subject = input('请输出计分学科')
                score = int(input('请输出成绩'))
                stu.add_score(subject, score)
                return
        print('学号有误')

    # 退出系统
    def quit(self):
        self.print_all_student()
        print('退出学生管理系统')
        exit()

    # 运行程序方法
    def run(self):
        while True:
            print('*******************学生管理系统**********************')
            print("""
            1.添加学生
            2.删除学生
            3.查看所有学生
            4.录入成绩
            5.退出
            """)
            choice = input('请输入操作序号')

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.del_student()
            elif choice == '3':
                self.print_all_student()
            elif choice == '4':
                self.input_score()
            elif choice == '5':
                self.quit()

# 启动程序
m1 = Magener()
m1.run()

