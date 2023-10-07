# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-9-2 10:51
# @Project : Learn.py
# @File    : 死锁.py

# 避免死锁：使用timeout
import time
from threading import Lock, Thread

lockA = Lock()
lockB = Lock()


class MyThreadA(Thread):
    def run(self):
        if lockA.acquire():
            print(self.name + '获取了A锁')
            time.sleep(0.1)
            if lockB.acquire(timeout=5):
                print(self.name + '又获取了B锁，现有A锁、B锁')
                lockB.release()
            lockA.release()


class MyThreadB(Thread):
    def run(self):
        if lockB.acquire():
            print(self.name + '获取了B锁')
            time.sleep(0.1)
            if lockA.acquire(timeout=5):
                print(self.name + '又获取了A锁，现有A锁、B锁')
                lockA.release()
            lockB.release()


if __name__ == '__main__':
    th1 = MyThreadA()
    th2 = MyThreadB()

    th1.start()
    th2.start()
