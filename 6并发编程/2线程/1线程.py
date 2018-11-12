"""
1进程
    进程是最小的内存分配单位
    进程中至少含有一个线程
    进程中可以开启多个线程
2线程
    线程是进程中的执行单位
    线程被CPU执行的最小单位
    线程之间资源共享
    开启一个线程所需要的时间要远远小于开启一个进程
python 与 2线程
    Cpython解释器在解释代码过程中容易产生数据不安全的问题
    GIL 全局解释器锁 锁的是线程
"""
from threading import Thread
import time

# def func(n):
#     time.sleep(1)
#     print(n)
#
# # 线程并发执行
# for i in range(10):
#     # 将这个函数注册到一个线程
#     t = Thread(target=func,args=(i,))
#     t.start()


"""
多线程中数据的共享
"""
def func(n):
    global a
    a += n
    print(a)

a = 100
lst = []
for i in range(10):
    # 注册线程并启动
    t = Thread(target=func,args=(i,))
    t.start()
    lst.append(t)
for t in lst:
    t.join()
print(a)