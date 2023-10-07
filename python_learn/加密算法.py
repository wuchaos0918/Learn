# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-29 23:21
# @Project : Learn.py
# @File    : 加密算法.py

# 加密算法

import hashlib
from Crypto.Cipher import AES
import base64

msg = '加密算法学习'
md5 = hashlib.md5(msg.encode('utf-8'))
print(md5)
print(md5.hexdigest())  # e7d3705b5cfa5c08e12f6160aa8f4cd6

sha1 = hashlib.sha1(msg.encode('utf-8'))
print(sha1)
print(sha1.hexdigest())

sha256 = hashlib.sha256(msg.encode('utf-8'))
print(sha256)
print(sha256.hexdigest())

# 系统登录
password1 = '123456'
sha256 = hashlib.sha256(password1.encode('utf-8'))
password1_sha256 = sha256.hexdigest()
list1 = [password1_sha256]


# 对长度不是16倍整数的数据进行补充加长
def add_to_16(par):
    par = par.encode()
    while len(par) % 16 != 0:
        par += b'\x00'
    return par


key = '1234567890123456'
text = '12345678'
model = AES.MODE_ECB  # AES模式
aes = AES.new(add_to_16(key), model)
iv = b'1234567890123456'
aes02 = AES.new(add_to_16(key), AES.MODE_CBC, iv)
en_text = aes.encrypt(add_to_16(text))
en_text02 = aes02.encrypt(add_to_16(text))
print("将(%s)加密：" % text)
print(en_text)
print(en_text02)
en_text = base64.encodebytes(en_text)  # 将返回的字节型数据进行base64编码
en_text02 = base64.encodebytes(en_text02)
print("将(%s)进行base64编码：" % text)
print(en_text)
print(en_text02)
en_text = en_text.decode('utf-8')  # 将字节型数据转换为python中的字符串类型
en_text02 = en_text02.decode('utf-8')
print("将(%s)转换为python中的字符串类型：" % text)
print(en_text)
print(en_text02)

pwd = input('请输入密码：')
sha256 = hashlib.sha256(pwd.encode('utf-8'))
pwd_sha256 = sha256.hexdigest()
print('固有密码：', list1)
print('输入密码：', pwd_sha256)
for i in list1:
    if pwd_sha256 == i:
        print('登录成功！')
    else:
        print('登录失败！')
