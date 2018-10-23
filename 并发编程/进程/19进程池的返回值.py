from multiprocessing import Pool
import time

def func(n):
    time.sleep(0.5)
    return n*n

if __name__ == '__main__':
    # 创建进程池
    pool = Pool(5)

    """
    map方法
    """
    res = pool.map(func,range(10))
    print(res)

    # lst = []
    # for i in range(10):
    #     """
    #     同步
    #     """
    #     # res = pool.apply(func,args=(i,))
    #     # print(res)
    #     """
    #     异步
    #     """
    #     res = pool.apply_async(func,args=(i,))
    #     lst.append(res)
    #     # print(res.get())    # 阻塞，等待一个进程的结果
    # for i in lst:
    #     print(i.get())

"""
可以用map解决的就用map，不能解决的用apply_async定制
"""