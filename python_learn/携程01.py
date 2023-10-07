# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-9-2 11:46
# @Project : Learn.py
# @File    : 携程01.py
import time


def task1():
    for i in range(3):
        print('A' + str(i))
        yield
        time.sleep(0.2)


def task2():
    for i in range(3):
        print('B' + str(i))
        yield
        time.sleep(0.2)


if __name__ == '__main__':
    g1 = task1()
    g2 = task2()

    while True:
        try:
            next(g1)
            next(g2)
        except Exception as E:
            print(E)
            break
