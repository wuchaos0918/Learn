# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-28 21:48
# @Project : Learn.py
# @File    : 私有化01.py

"""
私有化
封装：1、私有化属性 2、定义公有set和get方法
"""


class Student:
    # __age=18  #类属性
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__score = 60

    # 先有getXXX
    @property
    def age(self):
        return self.__age

    # 再设置setXXX，setXXX依赖getXXX
    @age.setter
    def age(self, age):
        if 0 < age <= 120:
            self.__age = age
        else:
            print('设置的年龄不在限制范围内')

    # 定义公有set和get方法
    # set赋值
    def setName(self, name):
        if len(name) == 6:
            self.__name = name
        else:
            print('应设置姓名长度为6位')

    # get取值
    def getName(self):
        return self.__name

    #
    # def setAge(self, age):
    #     if 0 < age <= 120:
    #         self.__age = age
    #     else:
    #         print('设置的年龄不在限制范围内')
    #
    # def getAge(self):
    #     return self.__age
    #
    # def setScore(self, score):
    #     if 0 <= score <= 100:
    #         self.__score = score
    #     else:
    #         print('设置的分数不在限制范围内')
    #
    # def getScore(self):
    #     return self.__score

    def __str__(self):
        return '姓名：{},年龄：{},考试分数：{}'.format(self.__name, self.__age, self.__score)


student01 = Student('HanMeiMei', 18)
student02 = Student('LiMing', 18)

print(student01)
print(student02)
# student01.setScore(98)
print(student01)
student01.setName('MaDongMei')
# student02.setAge(200)
print(student02.getName())
student01.age = 150
print(student01)
