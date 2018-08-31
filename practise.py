#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 导入需要的模块
import pygame
import sys
import time
import random
from pygame.locals import *
from math import pi

# 定义宽和高
WIDE = 600
HIGH = 400

# 初始化
pygame.init()

# 设置窗口
screen = pygame.display.set_mode((WIDE, HIGH))

# 设置窗口标题
pygame.display.set_caption('hello world')

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
color_tuple = (BLACK, WHITE, RED, GREEN, BLUE)

pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

pygame.draw.arc(screen, BLACK, [210, 75, 150, 125], 0, pi/2, 2)
pygame.draw.arc(screen, GREEN, [210, 75, 150, 125], pi/2, pi, 2)
pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi, 3*pi/2, 2)
pygame.draw.arc(screen, RED, [210, 75, 150, 125], 3*pi/2, 2*pi, 2)

pygame.draw.circle(screen, BLUE, [60, 250], 40)

# 程序主循环
while True:
    # 获取事件
    for event in pygame.event.get():
        # 判断事件是否为退出事件
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # 设置背景颜色
    screen.fill(WHITE)

    # 绘制一条线
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # x = [random.randint(0, 600), random.randint(0, 400)]
    # x1 = [random.randint(0, 600), random.randint(0, 400)]
    # y = [random.randint(0, 600), random.randint(0, 400)]
    # y1 = [random.randint(0, 600), random.randint(0, 400)]
    left = random.randint(0, 300)
    top = random.randint(0, 200)
    length = random.randint(10, 300)
    w = random.randint(50, 200)
    pygame.draw.rect(screen, color, [left, top, length, w], 2)

    time.sleep(0.1)

    # 更新画布
    pygame.display.update()



