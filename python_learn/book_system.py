# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-27 11:45
# @Project : Learn.py
# @File    : book_system.py


# 用户注册
def register():
    print('用户注册')
    username = input('输入用户名：')
    password = input('输入密码：')
    re_password = input('再次输入密码确认：')
    if password == re_password:
        with open(r'/book_system/user.txt', 'a') as stream:
            stream.write('{} {}\n'.format(username, password))
            print('用户{}注册成功！'.format(username))
    else:
        print('密码不一致！')


# 用户登录
def login():
    print('用户登录')
    username = input('输入用户名：')
    password = input('输入密码：')
    if username and password:
        with open(r'/book_system/user.txt', 'r') as stream:
            while True:
                user = stream.readline()
                if not user:
                    print('用户名或密码输入错误！')
                    break
                input_user = '{}{}\n'.format(username, password)
                if user == input_user:
                    print('用户{}登录成功！'.format(username))
                    break
    else:
        print('密码不一致！')


# 查询图书,utf-8才能解析中文
def show_books():
    print('-----图书馆里面的图书有-----')
    with open(r'/book_system/books.txt', 'r', encoding='utf-8') as stream:
        books = stream.readlines()
        for book in books:
            print(book, end='')


# 调用函数
register()
login()
show_books()
