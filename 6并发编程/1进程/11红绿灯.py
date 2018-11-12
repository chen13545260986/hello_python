from multiprocessing import Process
from multiprocessing import Event
import time
import random

def light(e):
    while True:
        if e.is_set():
            e.clear()
            print('\033[31m红灯亮了\033[0m')
        else:
            e.set()
            print('\033[32m绿灯亮了\033[0m')
        time.sleep(3)

def car(e,n):
    if not e.is_set():
        print('%s等待' % n)
        e.wait()    # 阻塞
    print('%s通过' % n)


if __name__ == '__main__':
    # 创建事件对象
    event = Event()
    # 创建进程对象
    p = Process(target=light,args=(event,))
    # 执行进程
    p.start()

    for i in range(20):
        p2 = Process(target=car,args=(event,i))
        p2.start()
        time.sleep(random.random())