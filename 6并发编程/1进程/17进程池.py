# 为什么会有进程池的概念
    # 效率
    # 每开启进程,开启属于这个进程的内存空间
    # 寄存器 堆栈 文件
    # 进程过多 操作系统的调度

# 进程池
    # python中的 先创建一个属于进程的池子
    # 这个池子指定能存放n个进程
    # 先讲这些进程创建好
# 更高级的进程池
    # n,m
    # 3   三个进程
    #     + 1进程
    # 20  20个
from multiprocessing import Pool
from multiprocessing import Process
import time

def func(n):
    print(n)

if __name__ == '__main__':
    # 创建进程池，最多允许5个进程一起运行
    pool = Pool(5)
    start1 = time.time()
    pool.map(func,range(100))   # 自带close和join
    t1 = time.time() - start1

    lst = []
    start2 = time.time()
    # 多进程一起执行
    for i in range(100):
        p = Process(target=func,args=(i,))
        p.start()
        lst.append(p)
    for i in lst:
        i.join()
    t2 = time.time() - start2

    print('进程池:',t1)
    print('多进程:',t2)