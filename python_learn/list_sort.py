# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-24 14:24
# @Project : Learn.py
# @File    : list_sort.py


# sort：排序，reverse：倒序
import random

numbers = []
for i in range(8):
    ran = random.randint(1, 100)
    numbers.append(ran)
print(numbers)
numbers.sort()
print('排序后的列表：%s' % numbers)
numbers.reverse()
print('倒序后的列表：%s' % numbers)

numbers = []
for i in range(8):
    ran = random.randint(1, 100)
    numbers.append(ran)
print(numbers)
for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            a = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = a
print(numbers)
