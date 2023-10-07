# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-9-2 10:05
# @Project : Learn.py
# @File    : 线程01.py

import threading

n = 1


def task1():
    global n
    for i in range(1000000):
        n += 1
    print('task1中n的值为：', n)


def task2():
    global n
    for i in range(1000000):
        n += 1
    print('task2中n的值为：', n)


if __name__ == '__main__':
    th1 = threading.Thread(target=task1())
    th2 = threading.Thread(target=task2())

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print('最后打印n的值为：', n)
