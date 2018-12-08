#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# Game_guess21.py
# author: Paul


# 1.导入标准库(使用随机方法)
import random
# 2.第三方的库(这段脚本不需要)
# 3.自定义的库(这段脚本不需要)


"""
 完善21点游戏（30分）

- 两个玩家，游戏开始先输入名字

- 用字典保存每个玩家信息：姓名，获胜次数

- 电脑随机产生2个数，每个玩家轮流猜1个数，与电脑随机两个数求和，最接近21的获胜

- 每轮结束显示玩家信息

- 按q退出游戏

"""

"""
- 选中一样的单词，比如conputer然后按CTRL+D
- 可多个同时编辑，ESC退出

"""

# 先输出一个欢迎界面

print('双人PK二十一点'.center(30, '*'))  # 居中，左右用*补齐


# 输入玩家姓名并写入字典

user_a = input('请输入姓名：')
user_b = input('请输入姓名：')

user_dict = {
    user_a: {'win': 0},
    user_b: {'win': 0}
}

#  来个循环输入功能

while True:

    computer_num1 = random.randint(1, 10) #随机生成一个数
    computer_num2 = random.randint(1, 10)
    usera_num = input(f'请{user_a}输入一个数字(输入q退出）:')
    userb_num = input(f'请{user_b}输入一个数字(输入q退出）:')
    if usera_num == 'q' or userb_num == 'q':  # 写while的时候要避免死循环，这里写一个退出语句
        print("退出游戏！")
        break
    else:
        user_a_sum = computer_num1 + computer_num2 + int(usera_num)  # 求和
        user_b_sum = computer_num1 + computer_num2 + int(userb_num)
        if abs(user_a_sum - 21) > abs(user_b_sum - 21):  # 判断绝对值大小
            print(f'电脑随机产生的两个数分别为{computer_num1}与{computer_num2}'.center(30, "*"))
            print(f'{user_a}输入的数字为{usera_num},{user_b}输入的数字为{userb_num},{user_b}WIN!')
            user_dict[user_b]['win'] += 1
            print(user_dict)
        else:
            print(f'电脑随机产生的两个数分别为{computer_num1}与{computer_num2}'.center(30, "*"))
            print(f'{user_a}输入的数字为{usera_num},{user_b}输入的数字为{userb_num},{user_a}WIN!')
            user_dict[user_a]['win'] += 1
            print(user_dict)