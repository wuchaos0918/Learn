# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-27 22:41
# @Project : Learn.py
# @File    : 生成器generator04.py


"""
协程：多任务交替执行
"""


def task1(n):
    for i in range(1, n):
        print('正在看第{}本书'.format(i))
        yield


def task2(n):
    for i in range(1, n):
        print('正在听第{}首歌'.format(i))
        yield


g1 = task1(5)
g2 = task2(5)

task_flag = True
while task_flag:
    try:
        next(g1)
        next(g2)
    except Exception as E:
        print(E)
        task_flag = False
