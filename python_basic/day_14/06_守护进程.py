# 什么是守护进程：一种依赖于主进程存在的子进程，主进程一旦结束，守护进程也会结束

# 守护进程的使用场景：
# 1、后台监控类任务
# 2、日志 、 统计 、 采样 等任务
# 3、辅助性陪跑任务

import os
from multiprocessing import Process
import time

def monitor():
    while True:
        try:
            with open('demo.txt', 'r', encoding='utf-8') as f:
                lines = sum(1 for line in f)
        except FileNotFoundError:
            lines = 0
        print(f'demo文件写入{lines}行')
        time.sleep(1)

if __name__ == '__main__':
    # daemon=True 表示p1是守护进程
    p1 = Process(target=monitor, daemon=True)
    p1.start()

    with open('demo.txt', 'a', encoding='utf-8') as f:
        for i in range(10):
            f.write(f'加薪{i}k\n')
            f.flush()
            time.sleep(1)

    print()     # 主进程执行完这句，守护进程p1就会被结束


