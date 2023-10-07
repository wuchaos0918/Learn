# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-9-2 11:09
# @Project : Learn.py
# @File    : 线程通信-生产者与消费者.py

import threading
import queue
import random
import time


def produce(q_produce):
    i = 0
    while i < 10:
        num = random.randint(1, 100)
        q_produce.put('生产者产生数据：%d' % num)
        print('生产者产生数据：%d' % num)
        time.sleep(1)
        i += 1
    q_produce.put(None)
    # 完成任务
    q_produce.task_done()


def consume(q_consume):
    while True:
        item = q_consume.get()
        if item is None:
            break
        print('消费者获取到：%s' % item)
        time.sleep(3)
    # 完成任务
    q_consume.task_done()


if __name__ == '__main__':
    q = queue.Queue(10)
    # arr = []

    # 创建生产者
    th_produce = threading.Thread(target=produce, args=(q,))
    th_produce.start()

    # 创建消费者
    th_consume = threading.Thread(target=consume, args=(q,))
    th_consume.start()

    th_produce.join()
    th_consume.join()
    print('END')
