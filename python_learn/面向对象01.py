# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-28 19:13
# @Project : Learn.py
# @File    : 面向对象01.py

"""
面向对象 类方法
"""


class Cat:
    type = '猫'

    # 通过__init__初始化的特征
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    # 动作：方法
    def eat(self, food):
        print('{}喜欢吃{}'.format(self.name, food))

    def catch_mouse(self, color, weight):
        print('{}抓住了一支{}{}斤的老鼠'.format(self.name, color, weight))

    def sleep(self, hour):
        if hour < 5:
            print('{}才睡觉{}个小时，继续睡觉'.format(self.name, hour))
        else:
            print('{}睡了{}小时，醒了去抓老鼠'.format(self.name, hour))


cat1 = Cat('Mimi', 2, '白色')
cat1.eat('猫粮')
cat1.catch_mouse('黑色', '0.2')
cat1.sleep(8)
print('-' * 20)
cat2 = Cat('Axe', 1, '黑色')
cat2.eat('小金鱼')
cat2.catch_mouse('灰色', '0.1')
cat2.sleep(4)
