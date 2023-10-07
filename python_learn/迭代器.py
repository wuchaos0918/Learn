# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-27 22:54
# @Project : Learn.py
# @File    : 迭代器.py

"""
迭代器 iter()
"""

from collections.abc import Iterable

list1 = [1, 3, 5, 7, 9]
f = isinstance(list1, Iterable)
print(f)

list1 = iter(list1)
print(next(list1))
print(next(list1))
