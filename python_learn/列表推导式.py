# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-27 21:09
# @Project : Learn.py
# @File    : 列表推导式.py

"""
列表推导式：格式[表达式 for 变量 in 旧列表] 或者 [表达式 for 变量 in 旧列表 if 条件]
"""

# 过滤长度小于等于3的人名
names = ['tom', 'lily', 'bob', 'cart', 'jack', 'steven']
result = [name for name in names if len(name) > 3]
print(result)

result = [name.capitalize() for name in names if len(name) > 3]
print(result)

# 查找1-100以内能被3和5整除的数
new_list = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(new_list)

# 0-9偶数，0-9奇数
new_list_02 = [(x, y) for x in range(10) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(new_list_02)


# 函数写法
def func():
    double_list = []
    for i in range(10):
        if i % 2 == 0:
            for j in range(10):
                if j % 2 != 0:
                    double_list.append((i, j))
    return double_list


x = func()
print(x)

# 列表反转
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list1 = [[i[0] for i in list1], [i[1] for i in list1], [i[2] for i in list1]]
print(new_list1)

"""
集合推导式 {}
"""

# 求列表里大于5的值（不重复）
list1 = [1, 2, 3, 5, 6, 7, 8, 6, 5, 3, 2, 1]
set1 = {x - 1 for x in list1 if x > 5}
print(set1)

"""
字典推导式
"""

# 反转字典的键和值
dict01 = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
new_dict01 = {value: key for key, value in dict01.items()}
print(new_dict01)
