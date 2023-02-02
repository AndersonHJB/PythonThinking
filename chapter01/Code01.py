# -*- coding: utf-8 -*-
# @Time    : 2023/2/1 10:14
# @Author  : AI悦创
# @FileName: Code01.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
import sys

import pygame  # 导入 pygame 库

# 进入游戏时需要加载游戏——可理解为：游戏初始化
pygame.init()  # 调用初始化函数

screen_width = 600  # 窗口宽度
screen_height = 400  # 窗口高度
screen_size = (screen_width, screen_height)  # 存放在我们的元组中

screen = pygame.display.set_mode(screen_size)  # screen 接收了 pygame 建立的对象，对象之后会学到。

# ------第一步代码完成，程序运行会有黑色窗口闪过------
# 要想程序持续运行，需要使用到循环
while True:
    # 在循环中，每循环一次就判断要不要退出
    for event in pygame.event.get():
        # 使用 for 循环获取当前 pygame 窗体的事件
        if event.type == pygame.QUIT:
            # 如果获取到的事件类型是 QUIT「退出」
            sys.exit()  # 那么调用系统退出
    # 每次判断完毕后，就要更新窗口画面
    pygame.display.update()  # update 意为更新
# ------第二步完成，现在窗口不会闪退，可以使用鼠标关闭------
