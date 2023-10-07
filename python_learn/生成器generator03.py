# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-27 22:20
# @Project : Learn.py
# @File    : 生成器generator03.py

def gen():
    i = 0
    while i < 5:
        temp = yield i
        print('temp:', temp)
        for x in range(temp):
            print('---->', x)
        print('*' * 20)
        i += 1
    return '没有更多的数据'


g = gen()
# send(value)项每次生成器中传递值，第一次需传递None
print(g.send(None))
n1 = g.send(3)
print('n1:', n1)
n2 = g.send(5)
print('n2:', n2)
print(g.send('呵呵'))
print()
