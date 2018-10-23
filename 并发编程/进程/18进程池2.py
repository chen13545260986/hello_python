from multiprocessing import Pool
import time
import os

def func(n):
    print('start func%s:' % n,os.getpid())
    time.sleep(1)
    print('end func%s' % n,os.getpid())

if __name__ == '__main__':
    # 创建进程池
    pool = Pool()   # 不指定数量就默认以计算机CPU的内核数
    for i in range(10):
        pool.apply_async(func, args=(i,))   # 异步执行
        # pool.apply(func, args=(i,))   # 同步执行
    # 关闭进程池
    pool.close()
    # 感知进程池中任务执行结束
    pool.join()