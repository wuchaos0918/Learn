# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-24 15:19
# @Project : Learn.py
# @File    : Glory_of_Kings.py

"""
王者荣耀角色管理
角色：姓名，性别，职业
添加角色
删除角色
修改角色
查询角色
显示所有角色
退出系统
"""

print('~~~~~欢迎进入王者荣耀角色管理系统~~~~~')
all_role = []
while True:
    choice = input('请选择功能：\n1.添加角色\n2.删除角色\n3.修改角色\n4.查询角色\n5.显示所有角色\n6.退出系统\n')
    # 添加角色
    if choice == '1':
        print('\t添加角色信息')
        name = input('\t角色名：')
        sex = input('\t性别：')
        job = input('\t职业：')
        role = [name, sex, job]
        all_role.append(role)
        print('\t成功添加{}到王者荣耀系统中\n'.format(name))
    # 删除角色
    elif choice == '2':
        print('\t删除角色信息：')
        flag = True
        while flag:
            role_name = input('\t输入角色名：')
            for role in all_role:
                if role_name in role:
                    answer = input('是否确认删除？Y/N')
                    if answer.upper() == 'Y':
                        all_role.remove(role)
                        print('成功删除角色：{}'.format(role_name))
                        flag = False
                        break
                    else:
                        print('取消删除角色：{}'.format(role_name))
                        break
                else:
                    print('系统不存在角色：{},请重新输入角色名'.format(role_name))
    # 修改角色
    elif choice == '3':
        print('\t修改角色信息：')
        flag = True
        while flag:
            role_name = input('\t输入角色名：')
            for role in all_role:
                if role_name in role:
                    answer = input('\t修改的信息\n\t1.角色名\n\t2.性别\n\t3.职业\n')
                    if answer == '1':
                        next_name = input('修改后的角色名：')
                        old_name = role[0]
                        role[0] = next_name
                        print('将角色{}的角色名由{}修改为{}'.format(old_name, old_name, role[0]))
                        flag = False
                        break
                    elif answer == '2':
                        next_sex = input('修改后的性别：')
                        old_sex = role[1]
                        role[1] = next_sex
                        print('将角色{}的性别由{}修改为{}'.format(role[0], old_sex, role[1]))
                        flag = False
                        break
                    elif answer == '3':
                        next_role = input('修改后的职业：')
                        old_job = role[2]
                        role[2] = next_role
                        print('将角色{}的职业由{}修改为{}'.format(role[0], old_job, role[2]))
                        flag = False
                        break
                else:
                    print('\t输入错误，请检查后重新输入')
        pass
    # 查询角色
    elif choice == '4':
        print('\t查询角色信息：')
        role_name = input('\t角色名：')
        for role in all_role:
            if role_name in role:
                print('\t存在此角色，角色信息如下：')
                print('\t{}{}{}'.format(role[0].ljust(10), role[1].ljust(10), role[2].ljust(10)))
            else:
                print('系统不存在角色：{},请重新输入角色名'.format(role_name))
        pass
    # 显示所有角色
    elif choice == '5':
        print('\t显示所有角色信息：')
        print('{}{}{}'.format('名称'.center(10), '性别'.center(10), '职业'.center(10)))
        for role in all_role:
            print(role[0].center(10), end='')
            print(role[1].center(10), end='')
            print(role[2].center(10), end='')
            print()
    # 退出系统
    elif choice == '6':
        print('退出系统！')
