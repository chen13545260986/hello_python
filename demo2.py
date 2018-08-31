#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 导入模块
import pygame
import time
import random
from pygame.locals import *

# 初始化pygame
pygame.init()

# 设置窗口的大小，单位为像素
screen = pygame.display.set_mode((500, 400))

# 设置窗口的标题
pygame.display.set_caption('Font')

filename = 'font/Arial Black.TTF'
size = 50
font = pygame.font.Font(filename, size)

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 主循环
flag = True
while flag:
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 配置要显示的文字
    text = font.render('hello world', True, color)

    # 获得要显示的对象的rect
    rect = text.get_rect()

    # 设置显示对象的坐标
    rect.center = (random.randint(0, 500), random.randint(0, 400))

    # 设置背景
    screen.fill(WHITE)

    # 绘制字体
    screen.blit(text, rect)

    # 遍历事件队列
    for event in pygame.event.get():
        # 如果为按键事件
        if event.type == KEYDOWN:
            # 如果按的是ESC键
            if event.key == K_ESCAPE:
                flag = False
        # 如果为退出事件
        elif event.type == QUIT:
            flag = False

    # 刷新屏幕
    pygame.display.update()

    time.sleep(0.1)



