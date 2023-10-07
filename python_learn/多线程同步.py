# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-9-2 10:30
# @Project : Learn.py
# @File    : 多线程同步.py

import threading
import time

lock = threading.Lock()

list1 = [0] * 10


def task1():
    # 获取线程锁，如果已经上锁，则等待锁的释放
    lock.acquire()  # 得到锁，阻塞
    for i in range(len(list1)):
        list1[i] = 1
        time.sleep(0.5)
    lock.release()  # 释放锁


def task2():
    lock.acquire()  # 得到锁，阻塞
    for i in range(len(list1)):
        print('---->', i)
        time.sleep(0.5)
    lock.release()  # 释放锁


if __name__ == '__main__':
    t1 = threading.Thread(target=task1())
    t2 = threading.Thread(target=task2())

    t1.start()
    t2.start()
