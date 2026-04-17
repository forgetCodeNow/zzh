

import os
from multiprocessing import Process
import time


def speak():
    try:
        for i in range(10):
            print(f'我再说第{i}句, 我是speak进程，我的进程id是{os.getpid()}，我的父进程id是{os.getppid()}')
            time.sleep(1)
    # 使用terminate强制结束进程，不会触发执行finally代码
    finally:
        pass


def study():
    for i in range(13):
        print(f'我学习的第{i}天, 我是study进程，我的进程id是{os.getpid()}，我的父进程id是{os.getppid()}')
        time.sleep(1)


if __name__ == '__main__':
    p1 = Process(target=speak)
    p2 = Process(target=study)

    p1.start()
    p2.start()

    time.sleep(3)

    p1.terminate()      # 强制结束p1进程，只写这个不一定会立刻结束，要加上阻塞进程，确认p1结束了再继续执行下面的代码
    p1.join()           # 阻塞当前进程，确保p1被结束
    print(p1.is_alive())

