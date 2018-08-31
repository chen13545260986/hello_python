#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 导入模块
import pygame
import random
import time
from pygame.locals import *

# 初始化
pygame.init()

# 设置帧率（屏幕每秒刷新的次数）
FPS = 30

# 获得pygame的时钟
fpsClock = pygame.time.Clock()

# 设置窗口大小
screen = pygame.display.set_mode((500, 400), 0, 32)

# 设置窗口标题
pygame.display.set_caption('animation')

# 定义颜色
WHITE = (255, 255, 255)

# 加载图片
img = pygame.image.load('images/fugu.png')

# 初始化位置
x = 0
y = 0
direction = 'right'
step = random.randint(10, 50)


def get_direction(f=False, d='up'):
    # 初始化图片的移动方向
    direct_tuple = ('up', 'down', 'left', 'right')
    # 随机获取方向
    m = random.randint(0, 3)
    direct = direct_tuple[m]

    if f:
        flags = True
        while flags:
            if direct == d:
                m = random.randint(0, 3)
                direct = direct_tuple[m]
            else:
                flags = False

    return direct


# 游戏主循环
flag = True
while flag:
    # 绘制屏幕颜色
    screen.fill(WHITE)

    # 判断移动的方向，并对相应的坐标做加减
    if direction == 'right':
        x += step
        if x >= 300:
            direction = get_direction(True, 'right')
        else:
            direction = get_direction()
    elif direction == 'down':
        y += step
        if y >= 200:
            direction = get_direction(True, 'down')
        else:
            direction = get_direction()
    elif direction == 'left':
        x -= step
        if x <= 0:
            direction = get_direction(True, 'left')
        else:
            direction = get_direction()
    else:
        y -= step
        if y <= 0:
            direction = get_direction(True, 'up')
        else:
            direction = get_direction()

    # 该方法将用于图片绘制到相应的坐标中
    screen.blit(img, (x, y))

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

    # 设置pygame时钟的间隔时间
    fpsClock.tick(FPS)

