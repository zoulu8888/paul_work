#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# Game_guess21.py
# author: Paul


# 1.导入标准库(这段脚本不需要)
# 2.第三方的库(这段脚本不需要)
from color_me import ColorMe
# 3.自定义的库(这段脚本不需要)


"""
 完善51备忘录程序（30分）

- 1.使用字典和列表嵌套结构表示多条记录

- 2.添加信息时，直接输入一句话，进行解析拆解，记录时间与事件

- 3.不同信息采用不同颜色输出

"""

# 先输出一个欢迎界面

print('欢迎使用51备忘录'.center(30, '*'))  # 居中，左右用*补齐

# 定义一个列表来存放字典数据

all_memo = []
is_add = True

while (is_add):
    one = {}  # 定义一个字典
    info = input('请输入需要记录的信息：')
    one['时间'] = info[info.find('点')-1:info.find('点')+1]
    one['事件'] = info[info.find('点')+1:]
    all_memo.append(one)
    blue1 = ColorMe(f'备忘录{all_memo}').blue()
    #print(f'备忘录{all_memo}')
    print (blue1)
    num = 0
    for i in all_memo:
        num += 1
        red1 = ColorMe(f'项目{num}:{i}').red()
        print(red1)
    green1 = ColorMe(f'共{len(all_memo)}个待办事项').green()
    print(green1)
    is_add = input('是否继续 Y/N：') == 'Y'
