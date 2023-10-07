# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-9-1 22:19
# @Project : Learn.py
# @File    : 进程池.py

import os
from multiprocessing import Pool
import time
from random import random


def task(task_name):
    print('开始做任务……', task_name)
    start = time.time()
    time.sleep(random() * 2)
    end = time.time()
    # print('完成任务{}，用时：{},进程id：{}'.format(task_name, (end - start), os.getpid()))
    return '完成任务{}，用时：{},进程id：{}'.format(task_name, (end - start), os.getpid())


container = []


def callback_func(n):
    container.append(n)


if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['听音乐', '吃饭', '洗澡', '打游戏', '散步', '睡觉', '看电视', '看书']

    for task1 in tasks:
        pool.apply_async(task, args=(task1,), callback=callback_func)
    pool.close()  # 任务结束
    pool.join()  # 任务开始

    for c in container:
        print(c)
    print('完成所有任务，任务结束！')

