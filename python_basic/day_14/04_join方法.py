# join方法：阻塞当前进程，等join前面的进程执行完，再往下执行
# join(timeout)，timeout参数是表示阻塞时间，单位是秒
# 注意点
# 1、p.join() 不是让p进程等待，而是让执行join代码的进程等待
# 2、当timeout时间到了，就不在等待了，并不是进程结束
# 3、join必须在start之前



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

if __name__ == '__main__':
    p1 = Process(target=speak)
    p2 = Process(target=study)

    p1.start()
    # p1.join()   # 写在这里就是把p1 和 p2分开执行，实现同步
    p2.start()
    p1.join(10)       # 写这p1 和 p2异步执行，后面的代码要等p1 和 p2执行完毕后再执行
    p2.join()

