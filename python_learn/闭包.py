# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-26 15:43
# @Project : Learn.py
# @File    : 闭包.py

a = 100


def outer():
    a = 200

    def inner():
        b = 300
        nonlocal a
        a += b
        print('我是内部函数', b)

    print(a)
    inner()


outer()
print(a)
