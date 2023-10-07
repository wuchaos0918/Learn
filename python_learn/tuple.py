# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-24 14:51
# @Project : Learn.py
# @File    : tuple.py


t1 = ()
print(type(t1))

t2 = ('aa',)
print(type(t2))

t3 = ('a', 'b', 'c', 'd', 'e', 'f')
print(t3)
print('-' * 30)
# index找元组中的元素位置
index = t3.index('e', 1, 5)
print(index)

if 'f' in t3:
    print('存在')
else:
    print('不存在')

for i in t3:
    print(i, end=' ')
# list(tuple)---->元组转列表
# tuple(list)---->列表转元组

t4 = list(t3)
print()
t4.append('g')
print(t4)
t5 = tuple(t4)
print(t5)
