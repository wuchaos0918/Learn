# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-24 11:02
# @Project : Learn.py
# @File    : list_del.py
"""
列表删除：pop remove clear
"""
import random

list1 = ['洗衣液', '牙膏', '牛奶', '火腿肠']
result1 = list1.pop()
print(result1)
print('列表1有%s' % list1)
i = random.randint(0, 3)
list2 = ['洗衣液', '牙膏', '面包', '火腿肠']
goods_del = list2[i]
print('列表2中有：{}'.format(goods_del))
if goods_del in list1:
    list1.remove(list2[i])
    print('从列表1中移除{},列表1还有{}'.format(goods_del, list1))
else:
    print('列表2的{}不在列表1中'.format(goods_del))
