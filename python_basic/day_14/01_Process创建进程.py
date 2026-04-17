import os
from multiprocessing import Process
import time


def speak():
    for i in range(10):
        print(f'我再说第{i}句, 我是speak进程，我的进程id是{os.getpid()}，我的父进程id是{os.getppid()}')
        time.sleep(1)


def study():
    for i in range(13):
        print(f'我学习的第{i}天, 我是study进程，我的进程id是{os.getpid()}，我的父进程id是{os.getppid()}')
        time.sleep(1)

# 一定要写if __name__ == '__main__'判断，
# 1、当创建子进程时，系统默认的时spawn 模式，并不会把父进程内存中的函数交给子进程
# 2、Python会启动一个全新的Python解释器，重新执行当前的.py文件（作为模块，所以__name__返回值就不是__main__，就不会再执行下面代码去创建子进程）
# 3、在执行过程中，重新定义一个speak函数，交给子进程（每个进程有自己的内存空间）
if __name__ == '__main__':
    # 创建Process的实例对象（进程对象）
    # 1、在子进程创建时就要指定好要执行的任务
    # 2、此时的p1 p2 只是代码的子进程，操作系统还没有真的创建这两个子进程
    p1 = Process(target=speak)
    p2 = Process(target=study)

    # 调用进程对象start()方法，会立刻向操作系统申请一个进程，并且会将该进程交由系统进行调度
    p1.start()
    p2.start()

