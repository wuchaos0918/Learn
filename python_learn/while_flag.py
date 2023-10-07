# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-24 10:21
# @Project : Learn.py
# @File    : while_flag.py

# 通过设置flag的值为True、False来结束While循环
flag = True
i = 1
while flag:
    print(i)
    i += 1
    if i > 10:
        flag = False
