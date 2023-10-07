# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-28 23:26
# @Project : Learn.py
# @File    : 继承关系01.py


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭……')

    def run(self):
        print(self.name + '正在跑步……')


class Student(Person):
    # 类如果不定义__init,则调用父类super class的__init__
    # 如果类继承父类也需要定义自己的__init__,
    # 就需要在当前类的__init__中调用父类的__init__
    def __init__(self, name, age, clazz):
        # 调用父类的init
        super().__init__(name, age)
        self.clazz = clazz

    def study(self, course):
        print('{}正在学习{}课程'.format(self.name, course))

    # 类如果自己定义方法，则不继承父类的方法
    def eat(self, food='青椒肉丝'):
        super().eat()  # 子类的方法也可以调用父类的方法
        print(self.name + '正在吃饭……喜欢吃{}'.format(food))


class Doctor(Person):
    def __init__(self, name, age, patients):
        super().__init__(name, age)
        self.patients = patients


class Employee(Person):
    def __init__(self, name, age, salary, manager):
        super().__init__(name, age)
        self.salary = salary
        self.manager = manager


s = Student('Tom', 20, 2)
s.run()
s.study('《Python基础》')
s.eat()
s.eat('鱼香肉丝')
e = Employee('Mike', 25, 50000, 'Gid')
e.eat()

lists = ['ZhangSan', 'LiSi', 'WangWu', 'ZhaoLiu']
d = Doctor('Lucy', 40, lists)
d.run()
