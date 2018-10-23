from multiprocessing import Process
from multiprocessing import Queue
import random
import time

# 生产者
def producer(q,name,food):
    for i in range(10):
        print('%s:%s生产了一个%s' % (i,name,food))
        f = food+str(i)
        q.put(f)
        time.sleep(random.randint(1,3))


# 消费者
def consumer(q,name):
    while True:
        food = q.get()
        if food is None:
            break
        else:
            print('%s消费了%s' % (name,food))

        time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    # 创建一个队列
    queue = Queue()
    # 创建进程执行producer方法
    p1 = Process(target=producer,args=(queue,'ming','cake'))
    p2 = Process(target=producer,args=(queue,'hong','icecream'))
    # 创建进程执行consumer方法
    c1 = Process(target=consumer,args=(queue,'white'))
    c2 = Process(target=consumer,args=(queue,'black'))
    # 执行进程
    p1.start()
    p2.start()
    c1.start()
    c2.start()
    # 等待p1和p2执行完之后,把None放到队列
    p1.join()
    p2.join()
    queue.put(None)
    queue.put(None)
