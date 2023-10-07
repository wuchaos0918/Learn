# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-24 23:46
# @Project : Learn.py
# @File    : 可变参数args.py

import random

a, *b, c = 1, 2, 3, 4, 5
print(a)
print(b)
print(c)


def get_print(*args):
    print(args)


def get_sum(*args):
    s = 0
    for i in args:
        s += i
    print(s)


get_print(1, 2, 3)
get_sum(1, 2, 3, 4)

"""
**kwargs 关键字参数
函数调用时必须传递关键字参数
才可以将其转换为key：value，将其装到字典中
"""


def show_book(**kwargs):
    print(kwargs)


show_book()
show_book(bookname='西游记', auther='吴承恩')


# 获取列表的最小组、最大值
def get_max_and_min(numbers):
    # 冒泡排序列表
    for i in range(0, len(numbers) - 1):
        for j in range(0, len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    # 获取列表的头尾，为最小值、最大值
    min_number = numbers[0]
    max_number = numbers[-1]
    return {'min_number': min_number, 'max_number': max_number}


def build_lists():
    result = []
    for i in range(10):
        x = random.randint(1, 100)
        result.append(x)
    return result


list1 = build_lists()
print(list1)
list2 = get_max_and_min(list1)
print(list2)
