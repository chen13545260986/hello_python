from threading import Thread
from threading import Lock
from threading import RLock
import time

"""
互斥锁
"""
# def func(lock):
#     global n
#     lock.acquire()
#     tmp = n
#     time.sleep(0.2)
#     n = tmp - 1
#     lock.release()
#
# n = 10
# # 实例化锁
# lock = Lock()
#
# t_lst = []
# for i in range(10):
#     # 实例化线程
#     t = Thread(target=func,args=(lock,))
#     t.start()
#     t_lst.append(t)
# # 监听子线程的结束
# for t in t_lst:
#     t.join()
# print(n)

"""
科学家吃面
"""
# noodle_lock = Lock()
# fork_lock = Lock()
# def eat1(name):
#     noodle_lock.acquire()
#     print('%s拿到面条啦'%name)
#     fork_lock.acquire()
#     print('%s拿到叉子了'%name)
#     print('%s吃面'%name)
#     fork_lock.release()
#     noodle_lock.release()
#
# def eat2(name):
#     fork_lock.acquire()
#     print('%s拿到叉子了'%name)
#     time.sleep(1)
#     noodle_lock.acquire()
#     print('%s拿到面条啦'%name)
#     print('%s吃面'%name)
#     noodle_lock.release()
#     fork_lock.release()
#
# Thread(target=eat1,args=('alex',)).start()
# Thread(target=eat2,args=('Egon',)).start()
# Thread(target=eat1,args=('bossjin',)).start()
# Thread(target=eat2,args=('nezha',)).start()

"""
递归锁(用来解决死锁问题)
"""
fork_lock = noodle_lock = RLock()   # 一个钥匙串上的两把钥匙
def eat1(name):
    noodle_lock.acquire()            # 一把钥匙
    print('%s拿到面条啦'%name)
    fork_lock.acquire()
    print('%s拿到叉子了'%name)
    print('%s吃面'%name)
    fork_lock.release()
    noodle_lock.release()

def eat2(name):
    fork_lock.acquire()
    print('%s拿到叉子了'%name)
    time.sleep(1)
    noodle_lock.acquire()
    print('%s拿到面条啦'%name)
    print('%s吃面'%name)
    noodle_lock.release()
    fork_lock.release()

Thread(target=eat1,args=('alex',)).start()
Thread(target=eat2,args=('Egon',)).start()
Thread(target=eat1,args=('bossjin',)).start()
Thread(target=eat2,args=('nezha',)).start()