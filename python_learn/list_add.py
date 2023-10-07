# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-24 10:28
# @Project : Learn.py
# @File    : list_add.py

# 超市添加商品
container = []
flag = True
while flag:
    print('添加商品')
    name = input('输入商品名称：')
    price = input('输入商品单价：')
    number = input('输入商品数量：')
    goods = [name, price, number]
    container.append(goods)
    answer = input('是否继续添加商品？（按Q或q退出，按其他键继续添加）')
    if answer.upper() == 'Q':
        flag = False
print(container)
# 打印商品列表，格式化打印
print('*' * 65)
print('{}{}{}'.format('商品名称'.center(20, '-'), '商品单价'.center(20), '商品数量'.center(20, '-')))
for goods in container:
    print('{}{}{}'.format(goods[0].center(20, '-'), goods[1].center(20), goods[2].center(20, '-')))
