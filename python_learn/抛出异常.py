# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-27 20:54
# @Project : Learn.py
# @File    : 抛出异常.py

"""
:raise 抛出异常
"""


def register():
    print('用户注册')
    username = input('输入用户名：')
    if len(username) < 6:
        raise Exception('用户名长度不能小于6位')
    else:
        print('输入的用户名是：', username)


try:
    register()
except Exception as E:
    print(E)
    print('注册失败！')
else:
    print('注册成功！')
