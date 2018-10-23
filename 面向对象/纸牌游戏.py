"""
纸牌游戏
"""
from collections import namedtuple
from random import choice
from random import shuffle
import json

class Cards:
    # 花色
    __color = ['桃花', '红心', '梅花', '方块']
    # 等级
    __level = [i for i in range(2, 11)] + list('JQKA')

    def __init__(self):
        Card = namedtuple('Card',['color', 'level'])
        self.__list = [Card(color,level) for color in self.__color for level in self.__level]

    def __len__(self):
        return len(self.__list)

    def __getitem__(self, item):
        return self.__list[item]

    def __setitem__(self, key, value):
        self.__list[key] = value

    def __str__(self):
        return json.dumps(cards.__list, ensure_ascii=False)

# 实例化纸牌对象
cards = Cards()
print(cards)
# 指定第一张牌
print(cards[0])
print('===')
# 抽牌
print(choice(cards))
print('===')
# 洗牌
shuffle(cards)
print(cards)
print(cards[0])
