# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-9-2 12:49
# @Project : Learn.py
# @File    : 概率测试.py

import random

nums = 1000000
list1 = []


def run(n):
    for i in range(n):
        num = 0
        for j in range(nums):
            result = random.randint(1, 100)
            # print(result)
            if result <= 40:
                num += 1
        total = num / nums
        list1.append(total)
        print(total)
    print(list1)


run(10)

# for i in range(nums):
#     result = random.randint(1, 2)
#     if result == 1:
#         num += 1
# total = num / nums
# print(total)
