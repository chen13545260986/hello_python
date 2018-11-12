"""
1进程 启动多个进程 进程之间是由操作系统负责调用
2线程 启动多个线程 真正被CPU执行的最小单位实际是线程
    开启一个线程 创建一个线程 寄存器 堆栈
    关闭一个线程
3协程
    本质上是一个线程
    能够在多个任务之间切换来节省一些IO时间
    协程中任务之间的切换也消耗时间,但是开销要远远小于进程线程之间的切换
"""
"""
greenlet：协程模块
"""
from greenlet import greenlet

def func1():
    print(1)
    g2.switch()
    print(3)
    g2.switch()

def func2():
    print(2)
    g1.switch()
    print(4)

g1 = greenlet(func1)
g2 = greenlet(func2)
g1.switch()
