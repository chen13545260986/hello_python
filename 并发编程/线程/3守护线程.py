"""
守护进程随着主进程代码的执行结束而结束
守护线程会在主线程结束之后，等待其他子线程的结束才结束

主进程在执行完自己的代码之后不会立即结束，而是等待子进程结束之后，回收子进程的资源
"""
from threading import Thread
import time

def func1():
    while True:
        time.sleep(1)
        print('*'*10)

def func2():
    print('in func2')
    time.sleep(5)

t1 = Thread(target=func1)
# 将t1设置为守护线程
t1.daemon = True
t1.start()
time.sleep(3)
t2 = Thread(target=func2)
t2.start()