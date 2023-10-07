# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-9-1 21:38
# @Project : Learn.py
# @File    : 进程01.py

import os
from multiprocessing import Process
from time import sleep


def task1(s, name):
    while True:
        sleep(s)
        print('这是任务1……', os.getpid(), '-----', os.getppid(), name)


def task2(s, name):
    while True:
        sleep(s)
        print('这是任务2……', os.getpid(), '-----', os.getppid(), name)


number = 1
if __name__ == '__main__':
    print(os.getpid())
    # 子进程
    p1 = Process(target=task1, name='任务1', args=(2, 'aa'))
    p1.start()
    print(p1.name)
    p2 = Process(target=task2, name='任务2', args=(2, 'bb'))
    p2.start()
    print(p2.name)

    while True:
        number += 1
        sleep(0.2)
        if number == 100:
            p1.terminate()
            p2.terminate()
            break
        else:
            print('---->number:', number)

    print('*' * 20)
