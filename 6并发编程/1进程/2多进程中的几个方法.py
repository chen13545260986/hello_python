"""
join():等待进程的结束
"""
from multiprocessing import Process
import time

def func(args1,args2):
    print('*'*args1)
    time.sleep(3)
    print('='*args2)


if __name__ == '__main__':
    # 实例化一个进程对象并启动
    p = Process(target=func,args=(10,20))
    p.start()
    # 等待进程结束
    p.join()
    print('执行完成')