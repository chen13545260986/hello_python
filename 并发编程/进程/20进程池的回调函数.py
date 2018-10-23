from multiprocessing import Pool
import os

def func1(n):
    print('in func1:',os.getpid())
    return n*n

def func2(m):
    print('in func2:',os.getpid())
    return m

if __name__ == '__main__':
    pool = Pool(5)

    for i in range(5):
        res = pool.apply_async(func1,args=(i,),callback=func2)
        print(res.get())
    print('主进程：',os.getpid())

"""
回调函数的参数为func1的返回值,并且回调函数回到主进程执行
"""