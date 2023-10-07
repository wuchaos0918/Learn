# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-26 15:32
# @Project : Learn.py
# @File    : test.py
import random

list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)

import numpy

# numpy.random.seed(0)
# p=numpy.array([0.1,0.9])
# i = 1
# while i < 10:
#     i += 1
#     index = numpy.random.choice(['Hit', 'Critical_Hit'], 10, p=[0.3, 0.7])
#     print(index)
#     print(index[0])
i = 1
while 1 < 10:
    i += 1
    result = random.randint(1, 3)
    print(result)
