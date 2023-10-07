# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-27 15:21
# @Project : Learn.py
# @File    : 异常处理.py

"""
异常机制
格式
try:
    可能出现异常的代码
expect 异常类型1：
    print(……)
expect 异常类型2：
    print(……)
expect Exception：
    print(……)
finally:
    无论是否有异常都会执行的代码

"""


def func():
    try:
        n1 = int(input('输入第一个数字：'))
        n2 = int(input('输入第二个数字：'))
        per = input('输入运算符号（+-*/）')
        result = None
        if per == '+':
            result = n1 + n2
        elif per == '-':
            result = n1 - n2
        elif per == '*':
            result = n1 * n2
        elif per == '/':
            result = n1 / n2
        else:
            print('符号输入错误！')

        # 测试删除空列表报错
        list1 = []
        list1.pop()

        # 测试打开不存在的文件报错
        with open(r'D:\Python\file', 'r') as stream:
            print(stream.read())

        print('运算结果为；', result)

    except ZeroDivisionError:
        print('除数不能为零！')
    except ValueError:
        print('必输输入数字！')
    except Exception as E:
        print('出错了！', E)


func()
