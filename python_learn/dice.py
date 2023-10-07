# -*- coding: UTF-8 -*-
# @Author  : Chaos-ThinkPad
# @Email   : WuChao0918@qq.com
# @Software: PyCharm
# @Time    : 2021-8-23 15:17
# @Project : first.py
# @File    : dice.py

# 投掷骰子
"""
扔3个骰子
玩家VS电脑
起始各20枚金币
起始各压1枚金币，投第一个骰子
显示玩家和电脑本次的点数和总点数
确认是否压两倍，或者放弃
投第二个骰子
显示玩家和电脑本次的点数和总点数
确认是否压两倍，或者放弃
投第商个骰子
显示玩家和电脑本次的点数和总点数
结算
"""
import random

p_coins = 7
m_coins = 7
print('玩家现有 %d 枚金币，电脑现有 %d 枚金币' % (p_coins, m_coins))
count = 0
while p_coins >= 0 and m_coins >= 0:
    start_msg = input('是否启动投掷骰子游戏:Y/N（停止游戏请输入Q）\n')
    if start_msg == 'Y' or start_msg == 'y':
        count += 1
        stake = 1
        print('*****第 %d 局游戏开始！*****\n玩家和电脑压注 %d 枚金币' % (count, stake))
        p_num_count = 0
        m_num_count = 0
        i = 1
        while i <= 3:
            p_num = random.randint(1, 6)
            m_num = random.randint(1, 6)
            print('第 %d 枚骰子已经掷出！\n玩家点数为： %d\n电脑点数为： %d\n' % (i, p_num, m_num))
            p_num_count += p_num
            m_num_count += m_num
            print('玩家总点数为： % d\n电脑总点数为： % d' % (p_num_count, m_num_count))
            i += 1
            if i == 2 or i == 3:
                msg = input('是否加倍：Y/N（弃权请输入Q）\n')
                if msg == 'Y' or msg == 'y':
                    stake *= 2
                    print('加倍！玩家和电脑压注 %d 枚金币' % stake)
                elif msg == 'N' or msg == 'n':
                    print('不加倍，玩家和电脑仍然压注 %d 枚金币' % stake)
                elif msg == 'Q' or msg == 'q':
                    print('玩家弃权！本局游戏认输！')
                    break
                else:
                    print('输入错误，请重新输入：\n')
        if p_num_count > m_num_count:
            p_coins += stake
            m_coins -= stake
            print('*****第 %d 局玩家获胜！*****\n'
                  '玩家赢得 %d 枚金币，现有 %d 枚金币\n'
                  '电脑输了 %d 枚金币，现有 %d 枚金币\n'
                  % (count, stake, p_coins, stake, m_coins))
        elif p_num_count == m_num_count:
            print('*****第 %d 局平局！双方筹码不变！*****' % count)
        else:
            p_coins -= stake
            m_coins += stake
            print('*****第 %d 局电脑获胜！*****\n'
                  '玩家输了 %d 枚金币，现有 %d 枚金币\n'
                  '电脑赢了 %d 枚金币，现有 %d 枚金币\n'
                  % (count, stake, p_coins, stake, m_coins))
    elif start_msg == 'Q' or start_msg == 'q':
        break
if p_coins > m_coins:
    print('经过 %d 局游戏，玩家赢得 %d 枚金币！电脑只剩下 %d 枚金币！\n'
          '*****玩家获胜！电脑失败！*****'
          % (count, p_coins, m_coins))
elif p_coins == m_coins:
    print('经过 %d 局游戏，玩家赢得 %d 枚金币！电脑赢得 %d 枚金币！\n'
          '*****双方打成平手！*****'
          % (count, p_coins, m_coins))
else:
    print('经过 %d 局游戏，玩家只剩下 %d 枚金币！电脑赢得 %d 枚金币！\n'
          '*****玩家失败！电脑获胜！*****'
          % (count, p_coins, m_coins))
