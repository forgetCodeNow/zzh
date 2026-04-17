import os
from multiprocessing import Process,Lock, RLock
import time


def speak(lock):
    for i in range(10):
        # 整个锁内部做的操作就是一个原子级操作，一次性执行完毕，不会被中断（报错除外）
        # 上锁动作,多次上锁必须多次解锁，否者就会死锁
        lock.acquire()
        lock.acquire()
        print(f'我再说第{i}句, 我是speak进程，我的进程id是{os.getpid()}，我的父进程id是{os.getppid()}')
        # 解锁动作
        lock.release()
        lock.release()
        time.sleep(1)


def study(lock):

    for i in range(13):
        # with上下文管理器，会自动调用lock.acquire() 和 lcok.release()
        with lock:
            print(f'我学习的第{i}天, 我是study进程，我的进程id是{os.getpid()}，我的父进程id是{os.getppid()}')
        time.sleep(1)

if __name__ == '__main__':
    # 普通锁，只能上锁一次
    lock = Lock()
    # 可多次上锁，会给上锁计数，上几次锁就要解几次锁，一般用这个
    rlock = RLock()

    p1 = Process(target=speak, args=(rlock,))
    p2 = Process(target=study, args=(rlock,))

    p1.start()
    p2.start()

