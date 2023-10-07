# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-27 21:46
# @Project : Learn.py
# @File    : 生成器generator01.py

"""
生成器generator
1.通过列表推导式得到生成器
"""
# [x for x in range(10000000)]
# [0,3,6,9,12,15,18,...,27]
g = (x * 3 for x in range(10))
print(type(g))  # generator
print(g)

# 方法1.调用__next__()方法得到元素
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print('-' * 20)

# 方法2.next(生成器对象)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
