# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-26 16:23
# @Project : Learn.py
# @File    : 装饰器.py

# 定义装饰器
def decorate(func):
    print('---->1')

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('刷漆')
        print('铺地板')
        print('买家具')
        print('精装修房子')

    print('---->2')
    return wrapper


@decorate
def house(address, area):
    print('{}是毛坯房……,面积{}平方'.format(address, area))


@decorate
def hotel(name, address, area=40):
    print('酒店的名字是{}，地址在{},面积{}平方'.format(name, address, area))


house('炜岸城', 100)
hotel('全季酒店', '北京国贸', 100)
