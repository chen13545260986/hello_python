#!/usr/bin/python
# -*- coding:UTF-8 -*-

# 导入模块
import pygame
import sys
from pygame.locals import *

# 定义颜色
WHITE = (255, 255, 255)

# 初始化Pygame
pygame.init()

# 设置窗口和标题
screen = pygame.display.set_mode((500, 400), 1, 32)
pygame.display.set_caption('Event')

# 设置背景颜色
screen.fill(WHITE)

# 游戏主循环
while True:
    # 遍历事件列表
    for event in pygame.event.get():
        # 用户按下关闭按钮
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # 用户按下ESC键
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

        # 获取鼠标当前的位置
        if event.type == MOUSEMOTION:
            print(event.pos)

        # 获取鼠标按下的位置
        if event.type == MOUSEBUTTONDOWN:
            print('鼠标按下：', event.pos)

        # 获取鼠标抬起的位置
        if event.type == MOUSEBUTTONUP:
            print('鼠标抬起：', event.pos)

        # 获取键盘按下事件
        if event.type == KEYDOWN:
            if event.key == K_w or event.key == K_UP:
                print('上')
            elif event.key == K_s or event.key == K_DOWN:
                print('下')
            elif event.key == K_a or event.key == K_LEFT:
                print('左')
            elif event.key == K_d or event.key == K_RIGHT:
                print('右')

    # 刷新屏幕
    pygame.display.update()
