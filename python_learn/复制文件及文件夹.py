# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-27 14:44
# @Project : Learn.py
# @File    : 复制文件及文件夹.py


import os


# 复制文件
def copy(src_path, target_path):
    # 获取文件夹里面的内容
    file_list = os.listdir(src_path)
    # 变量列表
    for file in file_list:
        # 拼接路径
        path = os.path.join(src_path, file)
        # 判断是文件夹还是文件
        if os.path.isdir(path):
            # 复制创建文件夹
            path1 = os.path.join(target_path, file)
            os.mkdir(path1)
            print('复制文件夹 {} 成功'.format(path1))
            # 递归调用copy
            copy(path, path1)
        else:
            # 不是文件夹则直接进行复制
            with open(path, 'rb') as stream:
                container = stream.read()
                path1 = os.path.join(target_path, file)
                with open(path1, 'wb') as w_stream:
                    w_stream.write(container)
                print('复制文件 {} 成功'.format(path1))
    print('文件及文件夹复制完成！')


# 设置文件复制的源路径和目标路径
s_path = r'/file/file1'
t_path = r'/file/file2'

# 调用文件复制函数
copy(s_path, t_path)
