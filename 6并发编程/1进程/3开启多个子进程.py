"""
多个进程之间执行没有顺序，且都是异步执行
"""
from multiprocessing import Process
import time

def func(args1,args2):
    print('*'*args1)
    time.sleep(3)
    print('='*args2)

if __name__ == '__main__':
    l = []
    for i in range(10):
        n = i+1
        p = Process(target=func,args=(n,n))
        # 将每个对象放到列表中
        l.append(p)
        p.start()

    # 等待所有进程都结束
    [i.join() for i in l]
    print('执行完成')