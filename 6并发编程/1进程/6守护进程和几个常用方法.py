"""
方法：
    terminate():结束一个进程，不是在执行之后立即生效，需要一个操作系统的响应过程
    is_alive():判断一个进程是否存在
属性：
    daemon:是否开启守护进程，即随着主进程的结束而结束
    name:进程的名字
    pid:进程号
"""
from multiprocessing import Process
import time

def func():
    while True:
        print('i am still alive')
        time.sleep(1)


if __name__ == '__main__':
    # 实例化并启动进程
    p = Process(target=func)
    p.daemon = True  # 设置子进程为守护进程
    p.start()

    for i in range(10):
        print(i)
        time.sleep(1)