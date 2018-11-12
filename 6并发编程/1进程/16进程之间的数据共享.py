from multiprocessing import Process
from multiprocessing import Manager
from multiprocessing import Lock

def func(d,l):
    # 加锁
    l.acquire()
    d['count'] -= 1
    # 解锁
    l.release()

if __name__ == '__main__':
    # 实例化锁
    lock = Lock()
    # 实例化Manager
    m = Manager()
    # 共享字典
    dic = m.dict({'count':100})
    lst = []
    for i in range(50):
        p = Process(target=func,args=(dic,lock))
        p.start()
        lst.append(p)
    # 等待所有子进程结束
    for i in lst:
        i.join()
    print(dic)