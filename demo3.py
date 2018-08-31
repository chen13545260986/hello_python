#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 导入模块
import pygame
from pygame.locals import *

# 初始化pygame
pygame.init()

# 设置窗口
screen = pygame.display.set_mode((500, 400))

# 设置窗口标题
pygame.display.set_caption('audio')

# 定义颜色
WHITE = (255, 255, 255)

# 设置背景
screen.fill(WHITE)

# 加载背景音乐文件
pygame.mixer.music.load('music/10537.wav')

# 播放背景音乐，第一个参数为播放的次数（-1表示无限循环），第二个参数是设置播放的起点（单位为秒）
pygame.mixer.music.play(1, 0.0)

# 主循环
flag = True
while flag:
    # 遍历事件队列
    for event in pygame.event.get():
        # 如果为按键事件
        if event.type == KEYDOWN:
            # 如果按的是ESC键
            if event.key == K_ESCAPE:
                pygame.mixer.music.stop()
                flag = False
        # 如果为退出事件
        elif event.type == QUIT:
            pygame.mixer.music.stop()
            flag = False

    # 刷新屏幕
    pygame.display.update()
