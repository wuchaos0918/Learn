# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-27 21:56
# @Project : Learn.py
# @File    : 生成器generator02.py

g = (x * 3 for x in range(10))

while True:
    try:
        i = next(g)
        print(i)
    except Exception as E:
        print(E)
        print('没有更多元素了……')
        break


# 当函数中出现yield关键字时，说明函数变成了生成器
def func():
    n = 0
    while True:
        n += 1
        print(n)
        yield n  # return n + 暂停


# 直接调用函数不会执行
func()
# 使用next()方法执行函数
g = func()
next(g)
next(g)
next(g)


# 斐波那契数列
def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        # print(b)
        yield b
        a, b = b, a + b
        n += 1
    return '没有更多元素……'


g = fib(8)
print('*' * 20)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

