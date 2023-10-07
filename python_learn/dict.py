# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-24 16:19
# @Project : Learn.py
# @File    : dict.py

book01 = {'书名': '《三体》', '作者': '刘慈欣', '出版社': '***出版社'}
print(book01)
book01['书名'] = '《史记》'
print(book01)
book01.pop('出版社')
print(book01)

books = [{'书名': '《三体》', '作者': '刘慈欣', '出版社': '***出版社'},
         {'书名': '《史记》', '作者': '司马迁', '出版社': '***出版社'}]
value = book01.get('书名')
print(value)
print(list(book01.values()))
print(list(book01.keys()))
print(books)
for book in books:
    book.pop('出版社')
print(books)
