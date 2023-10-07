# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-26 11:36
# @Project : Learn.py
# @File    : 借书.py

"""
输入书籍名称后提示用户登录
如果登录成功就借书成功
登录失败则提示重新登录
函数内可以用:param xxx的方式写参数注释
"""

is_login = False


def login(username, password):
    """

    :param username: 账号
    :param password: 密码
    :return: 无返回参数
    """
    if username == 'admin' and password == '123456':
        print('登录成功')
        global is_login
        is_login = True


def borrow_books(book_name):
    if is_login:
        print('成功借阅{}'.format(book_name))
    else:
        print('借阅{}失败，用户未登录\n请登录'.format(book_name))
        username = input('用户名：')
        password = input('密码：')
        login(username, password)


borrow_books('草房子')
borrow_books('草房子')
