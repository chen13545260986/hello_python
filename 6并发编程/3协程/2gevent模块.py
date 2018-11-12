from gevent import monkey;monkey.patch_all()
import gevent
import time

# def func1():
#     print('start1')
#     time.sleep(1)
#     print('end1')
#
# def func2():
#     print('start2')
#     time.sleep(1)
#     print('end2')
#
# g1 = gevent.spawn(func1)
# g2 = gevent.spawn(func2)
# g1.join()
# g2.join()
"""
进程和线程的任务切换由操作系统完成
协程任务之间的切换由程序（代码）完成，只有遇到协程模块能识别的IO操作的时候，程序才会进行任务切换，实现并发的效果
"""

"""
同步和异步的比较
"""
def task():
    time.sleep(1)
    print(123)

def sync():
    for i in range(10):
        task()

def asyn():
    lst = []
    for i in range(10):
        # 将task方法放入协程中
        g = gevent.spawn(task)
        lst.append(g)
    gevent.joinall(lst)

sync()
asyn()