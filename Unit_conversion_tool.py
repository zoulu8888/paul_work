#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# Unit conversion tool.py
# author: Paul


# 1.导入标准库(这段脚本不需要)
# 2.第三方的库(这段脚本不需要)
# 3.自定义的库(这段脚本不需要)


"""
案例：单位转换器

一 完善单位转换器程序（30分）

- 1.根据输入内容判断单位类型

- 2.完成温度互转，华氏温度与摄氏温度，

- 3.完成长度互转，中国与美国长度单位

- 4.完成货币互转，美元与人民币（汇率以你作业当天为准）

"""


# 先输出一个欢迎界面

print('欢迎使用万能转换器'.center(30, '*'))  # 居中，左右用*补齐


# 现在应该要有一个输出目录来让用户选择需要哪种转换
tool_menu = {     
    'T': '温度转换',  # 字典换行别忘了逗号
    'L': '长度转换',
    'C': '货币转换'
}

for k, v in tool_menu.items():  # 循环语句别忘了冒号
    print(k, v)


# 目录有了，现在写一个输入，知道用户的选择
user_choose = input('请选择需要转换的类型:')
user_choose = user_choose.upper()  # 加一个大小写转换，避免输入小写出错
# 接着判断选择了什么，就跳转到相应的模块中
if user_choose == 'T':
    temp = input('请输入温度（示例1C或1F）:')
    temp = temp.upper()  # 加一个大小写转换，避免输入小写出错
    if temp.endswith('C'):
        temp = float(temp.strip('C').strip('F'))  # 去掉尾部的C，如果有的化再去掉尾部的F
        Tf = (9/5) * temp + 32
        print(f'当前输入的摄氏度{temp}C转换结果为{Tf}F'.center(30, "*"))
    elif temp.endswith('F'):
        temp = float(temp.strip('F').strip('C'))
        Ft = (5/9) * (temp - 32)
        print(f'当前输入的华氏度{temp}F转换结果为{Ft}C'.center(30, "*")) 
    else:
        print('输入错误，请重新输入（示例1C或1F）'.center(30, "!"))  # 都不是就输出错误，给出示范
if user_choose == 'L':
    temp = input('请输入需要转换的长度（示例1M或1FT):')
    temp = temp.upper()
    if temp.endswith('M'):
        temp = float(temp.strip('M').strip('FT'))
        FT = 3.2808 * temp
        print(f'当前输入的{temp}米转换结果为{FT}英寸'.center(30, "*"))
    elif temp.endswith('FT'):
        temp = float(temp.strip('FT').strip('M'))
        M = 0.3048 * temp
        print(f'当前输入的{temp}英寸转换结果为{M}米'.center(30, "*"))
    else:
        print('输入错误，请重新输入（示例1M或1FT）'.center(30, "!"))  # 都不是就输出错误，给出示范
if user_choose == 'C':
    temp = input('请输入需要转换的货币（示例1人民币或1美元):')
    if temp.endswith('人民币'):
        temp = float(temp.strip('人民币'))
        dollor = temp * 0.1455
        print(f'当前输入的{temp}人民币转换结果为{dollor}美元'.center(30, "*"))
    elif temp.endswith('美元'):
        temp = float(temp.strip('美元'))
        rmb = temp * 6.8733
        print(f'当前输入的{temp}美元转换结果为{rmb}人民币'.center(30, "*"))
    else:
        print('输入错误，请重新输入（示例1人民币或1美元）'.center(30, "!"))  # 都不是就输出错误，给出示范
else:
    print('输入错误，请重新输入（示例T,L,C）'.center(30, "!"))  # 都不是就输出错误，给出示范