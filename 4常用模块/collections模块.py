# collections模块:python中的扩展数据类型

from collections import namedtuple
from collections import deque

# namedtuple：可命名元组
Point = namedtuple('point', ['x', 'y'])
p1 = Point(1, 2)
p2 = Point(3, 2)
print(p1.x)
print(p1.y)
print(p1, p2)

# deque:双端队列
#

