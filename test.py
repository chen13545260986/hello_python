#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 向sys模块借一个exit函数用来退出程序
from sys import exit
# 导入pygame库
import pygame
# 导入一些常用的函数和常量
from pygame.locals import *

bg_img = 'images/sushiplate.jpg'
fish_img = 'images/fugu.png'

# 初始化pygame,为使用硬件做准备
pygame.init()

# 创建了一个窗口
screen = pygame.display.set_mode((640, 480), RESIZABLE, 32)
# 设置窗口标题
pygame.display.set_caption("Hello, World!")

# 加载并转换图像
background = pygame.image.load(bg_img).convert()
mouse_cursor = pygame.image.load(fish_img).convert_alpha()

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件后退出程序
            exit()

    # 将背景图画上去
    screen.blit(background, (0, 0))

    # 获得鼠标位置
    x, y = pygame.mouse.get_pos()
    # 计算光标的左上角位置
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    # 把光标画上去
    screen.blit(mouse_cursor, (x, y))

    # 刷新一下画面
    pygame.display.update()
