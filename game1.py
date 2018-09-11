#!/usr/bin/python
# -*- coding:UTF-8 -*-

# 导入模块
import pygame
from pygame.locals import *
import random
import time
import sys

# 定义常量
FPS = 25
WINDOW_WIDTH = 640  # 整个游戏屏幕的宽
WINDOW_HIGH = 480   # 整个游戏屏幕的高
BOX_SIZE = 20   # 小格子的宽和高
BOARD_WIDTH = 10  # 游戏窗口本身有10个方块的宽度
BOARD_HIGH = 20   # 游戏窗口本身有20个方块的高度
BLANK = '.'  # 表示空白空格

MOVE_SIDEWAYS_FREQ = 0.15
MOVE_DOWN_FREQ = 0.1

X_MARGIN = int((WINDOW_WIDTH - BOARD_WIDTH * BOX_SIZE) / 2)  # 220
TOP_MARGIN = WINDOW_HIGH - BOARD_HIGH * BOX_SIZE - 5  # 75

# 颜色
WHITE = (255, 255, 255)
GRAY = (185, 185, 185)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_RED = (175, 20, 20)
GREEN = (0, 255, 0)
LIGHT_GREEN = (20, 175, 20)
BLUE = (0, 0, 255)
LIGHT_BLUE = (20, 20, 175)
YELLOW = (155, 155, 0)
LIGHT_YELLOW = (175, 175, 20)

# 颜色设置
BORDER_COLOR = BLUE
BG_COLOR = BLACK
TEXT_COLOR = WHITE
TEXT_SHADOW_COLOR = GRAY
COLORS = (BLUE, GREEN, RED, YELLOW)
LIGHT_COLORS = (LIGHT_BLUE, LIGHT_GREEN, LIGHT_RED, LIGHT_YELLOW)
assert len(COLORS) == len(LIGHT_COLORS)

TEMPLATE_WIDTH = 5
TEMPLATE_HIGH = 5

# 方块的形状
S_SHAPE = [
    [
        '.....',
        '.....',
        '..00.',
        '.00..',
        '......'
    ],
    [
        '.....',
        '..0..',
        '..00.',
        '...0.',
        '.....'
    ]
]
Z_SHAPE = [
    [
        '.....',
        '.....',
        '.00..',
        '..00.',
        '......'
    ],
    [
        '.....',
        '..0..',
        '.00..',
        '.0...',
        '.....'
    ]
]
I_SHAPE = [
    [
        '..0..',
        '..0..',
        '..0..',
        '..0..',
        '......'
    ],
    [
        '.....',
        '.....',
        '0000.',
        '.....',
        '......'
    ]
]
O_SHAPE = [
    [
        '.....',
        '.....',
        '.00..',
        '.00..',
        '......'
    ]
]
J_SHAPE = [
    [
        '.....',
        '..0..',
        '..0..',
        '.00..',
        '......'
    ],
    [
        '.....',
        '.0...',
        '.000.',
        '.....',
        '......'
    ],
    [
        '.....',
        '..00.',
        '..0..',
        '..0..',
        '......'
    ],
    [
        '.....',
        '.....',
        '.000.',
        '...0.',
        '......'
    ]
]
L_SHAPE = [
    [
        '.....',
        '..0..',
        '..0..',
        '..00.',
        '......'
    ],
    [
        '.....',
        '.....',
        '.000.',
        '.0...',
        '......'
    ],
    [
        '.....',
        '.00..',
        '..0..',
        '..0..',
        '......'
    ],
    [
        '.....',
        '...0.',
        '.000.',
        '.....',
        '......'
    ]
]
T_SHAPE = [
    [
        '.....',
        '..0..',
        '.000.',
        '.....',
        '......'
    ],
    [
        '.....',
        '..0..',
        '..00.',
        '..0..',
        '......'
    ],
    [
        '.....',
        '.....',
        '.000.',
        '..0..',
        '......'
    ],
    [
        '.....',
        '..0..',
        '.00..',
        '..0..',
        '......'
    ]
]

# 方块集合
PIECES = {
    'S': S_SHAPE,
    'Z': Z_SHAPE,
    'J': J_SHAPE,
    'L': L_SHAPE,
    'I': I_SHAPE,
    'O': O_SHAPE,
    'T': T_SHAPE
}


# 定义主函数
def main():
    global FPS_CLOCK, DISPLAY_SURF, BASIC_FONT, BIG_FONT  # 全局化变量
    pygame.init()  # 初始化pygame
    FPS_CLOCK = pygame.time.Clock()  # 创建一个对象来帮助跟踪时间
    DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HIGH))
    BASIC_FONT = pygame.font.Font('font/Arial Black.TTF', 18)
    BIG_FONT = pygame.font.Font('font/Arial Black.TTF', 100)
    pygame.display.set_caption('Tetris')

    # 游戏主循环
    while True:
        # 播放音乐
        pygame.mixer.music.load('music/4296.wav')
        pygame.mixer.music.play(-1, 0.0)
        # 运行游戏
        run_game()
        # 游戏结束，音乐停止，显示game over
        pygame.mixer.music.stop()
        # showTextScreen('Game Over')


def run_game():
    board = get_black_board()
    last_move_down_time = time.time()
    last_move_sideways_time = time.time()
    last_fall_time = time.time()
    moving_down = False
    moving_left = False
    moving_right = False
    score = 0
    # 等级和下降速度
    level, fall_freq = calculate_level_and_fall_freq(score)
    # 获取
    falling_piece = get_new_piece()
    next_piece = get_new_piece()

    while True:
        if falling_piece is None:
            falling_piece = next_piece
            next_piece = get_new_piece()
            last_fall_time = time.time()

        # 监控退出事件
        check_for_quit()

        # 设置背景颜色
        DISPLAY_SURF.fill(BG_COLOR)

        if time.time() - last_fall_time > fall_freq:
            if not is_valid_position(board, falling_piece, 1):
                # falling piece has landed, set it on the board
                addToBoard(board, falling_piece)
                score += removeCompleteLines(board)
                level, fall_freq = calculateLevelAndFallFreq(score)
                falling_piece = None
            else:
                # piece did not land, just move the piece down
                falling_piece['y'] += 1
                last_fall_time = time.time()

        # 画游戏区域
        draw_board(board)
        # 画等级和评分
        draw_status(score, level)
        # 画下一个模板
        draw_next_piece(next_piece)
        if falling_piece is not None:
            draw_piece(falling_piece)
        # 更新屏幕
        pygame.display.update()


def get_black_board():
    board = []
    for i in range(BOARD_WIDTH):
        board.append([BLANK] * BOARD_HIGH)
    return board


def calculate_level_and_fall_freq(score):
    level = int(score / 10) + 1
    fall_freq = 0.27 - (level * 0.02)
    return level, fall_freq


def get_new_piece():
    shape = random.choice(list(PIECES.keys()))
    new_piece = {
        'shape': shape,
        'rotation': random.randint(0, len(PIECES[shape]) - 1),
        'x': int(BOARD_WIDTH / 2) - int(TEMPLATE_WIDTH / 2),
        'y': -2,
        'color': random.randint(0, len(COLORS) - 1)
    }
    return new_piece


def check_for_quit():
    for event in pygame.event.get():
        # 用户按下关闭按钮
        if event.type == QUIT:
            terminate()
        # 用户按下ESC键
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            terminate()

        # 将其他按键事件放回队列
        pygame.event.post(event)


def terminate():
    pygame.quit()
    sys.exit()


def draw_board(board):
    # 画一个空心的矩形
    pygame.draw.rect(DISPLAY_SURF, BORDER_COLOR, (X_MARGIN - 3, TOP_MARGIN - 7, (BOARD_WIDTH * BOX_SIZE) + 8,
                                                  (BOARD_HIGH * BOX_SIZE) + 8), 5)
    # 画一个实心的矩形
    pygame.draw.rect(DISPLAY_SURF, BG_COLOR, (X_MARGIN, TOP_MARGIN, BOX_SIZE * BOARD_WIDTH, BOX_SIZE * BOARD_HIGH))

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HIGH):
            draw_box(x, y, board[x][y])


def draw_box(box_x, box_y, color, pixel_x=None, pixel_y=None):
    if color == BLANK:
        return

    if pixel_x is None and pixel_y is None:
        pixel_x, pixel_y = convert_to_pixel_cords(box_x, box_y)

    pygame.draw.rect(DISPLAY_SURF, COLORS[color], (pixel_x + 1, pixel_y + 1, BOX_SIZE - 1, BOX_SIZE - 1))
    pygame.draw.rect(DISPLAY_SURF, LIGHT_COLORS[color], (pixel_x + 1, pixel_y + 1, BOX_SIZE - 4, BOX_SIZE - 4))


def convert_to_pixel_cords(box_x, box_y):
    return (X_MARGIN + (box_x * BOX_SIZE)), (TOP_MARGIN + (box_y * BOX_SIZE))


def draw_status(score, level):
    # 画分数
    score_surf = BASIC_FONT.render('Score: %s' % score, True, TEXT_COLOR)
    score_rect = score_surf.get_rect()
    score_rect.topleft = (WINDOW_WIDTH - 150, 20)
    DISPLAY_SURF.blit(score_surf, score_rect)

    # 画等级
    level_surf = BASIC_FONT.render('Level: %s' % level, True, TEXT_COLOR)
    level_rect = level_surf.get_rect()
    level_rect.topleft = (WINDOW_WIDTH - 150, 50)
    DISPLAY_SURF.blit(level_surf, level_rect)


def draw_next_piece(piece):
    # draw the "next" text
    next_surf = BASIC_FONT.render('Next:', True, TEXT_COLOR)
    next_rect = next_surf.get_rect()
    next_rect.topleft = (WINDOW_WIDTH - 120, 80)
    DISPLAY_SURF.blit(next_surf, next_rect)
    # draw the "next" piece
    draw_piece(piece, WINDOW_WIDTH - 120, 100)


def draw_piece(piece, pixel_x=None, pixel_y=None):
    shape_to_draw = PIECES[piece['shape']][piece['rotation']]
    if pixel_x is None and pixel_y is None:
        pixel_x, pixel_y = convert_to_pixel_cords(piece['x'], piece['y'])

        # draw each of the boxes that make up the piece
    for x in range(TEMPLATE_WIDTH):
        for y in range(TEMPLATE_HIGH):
            if shape_to_draw[y][x] != BLANK:
                draw_box(None, None, piece['color'], pixel_x + (x * BOX_SIZE), pixel_y + (y * BOX_SIZE))


def is_valid_position(board, piece, adj_x=0, adj_y=0):
    # Return True if the piece is within the board and not colliding
    for x in range(TEMPLATE_WIDTH):
        for y in range(TEMPLATE_HIGH):
            is_above_board = y + piece['y'] + adj_y < 0
            if is_above_board or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                continue
            if not is_on_board(x + piece['x'] + adj_x, y + piece['y'] + adj_y):
                return False
            if board[x + piece['x'] + adj_x][y + piece['y'] + adj_y] != BLANK:
                return False
    return True


def is_on_board(x, y):
    return x >= 0 and x < BOARD_WIDTH and y < BOARD_HIGH


main()
