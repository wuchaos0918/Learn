# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-11-24 13:34
# @Project : Learn.py
# @File    : encrypte.py

import hashlib
randomKey = '54b53072540eeeb8f8e9343e71f28176_25138a2b-c505-4271-aae3-020afb45dd67'
realm = 'TheNextService'
userName = 'system'
password = 'Gzdh@666'
# 一共计算五次MD5
signature = hashlib.md5(password.encode())
print(signature)
m = userName + signature
signature = hashlib.md5(m.encode())
print(signature)
signature = hashlib.md5(signature)
print(signature)
m=userName+':'+realm+':'+signature
signature=hashlib.md5(m.encode())
print(signature)
m=signature+':'+randomKey
signature=hashlib.md5(m.encode())
print(signature)
