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

m = 1  # 不可变类型
list1 = []  # 可变类型


def task1(s, name):
    global m
    while True:
        sleep(s)
        m += 1
        list1.append(str(m) + 'task1')
        print('这是任务1……', m, name, list1)


def task2(s, name):
    global m
    while True:
        sleep(s)
        m += 1
        list1.append(str(m) + 'task1')
        print('这是任务2……', m, name, list1)


if __name__ == '__main__':
    print(os.getpid())
    # 子进程
    p1 = Process(target=task1, name='任务1', args=(1, 'aa'))
    p1.start()

    p2 = Process(target=task2, name='任务2', args=(1, 'bb'))
    p2.start()

    while True:
        sleep(1)
        m += 1
        print('---->main:', m)
        if m == 20:
            p1.terminate()
            p2.terminate()
            break

    print('*' * 20)
