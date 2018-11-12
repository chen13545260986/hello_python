"""
用锁的原理实现，内置了一个计数器
在同一时间，只能有指定数量的进程执行某一段被控制的代码
"""
from multiprocessing import Process
from multiprocessing import Semaphore
import time

def func(n,s):
    s.acquire()

    print('%s走进了房间' % n)
    time.sleep(3)
    print('%s走出了房间' % n)

    s.release()


if __name__ == '__main__':
    # 实例化信号量
    sem = Semaphore(4)

    for i in range(20):
        p = Process(target=func,args=(i,sem))
        p.start()