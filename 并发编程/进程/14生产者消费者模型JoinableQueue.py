from multiprocessing import Process
from multiprocessing import JoinableQueue
import random
import time

# 生产者
def producer(q,name,food):
    for i in range(10):
        print('%s:%s生产了一个%s' % (i,name,food))
        f = food+str(i)
        q.put(f)
        time.sleep(random.randint(1,3))

    # 阻塞，直到队列中的所有数据被消耗
    q.join()


# 消费者
def consumer(q,name):
    while True:
        food = q.get()
        print('%s消费了%s' % (name,food))

        time.sleep(random.randint(1, 3))
        # 处理完一个就计数一次
        q.task_done()


if __name__ == '__main__':
    # 创建一个队列
    queue = JoinableQueue()
    # 创建进程执行producer方法
    p1 = Process(target=producer,args=(queue,'ming','cake'))
    p2 = Process(target=producer,args=(queue,'hong','icecream'))
    # 创建进程执行consumer方法
    c1 = Process(target=consumer,args=(queue,'white'))
    c2 = Process(target=consumer,args=(queue,'black'))
    # 执行进程
    p1.start()
    p2.start()
    # 把消费者设置为守护进程
    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()
    # 等待p1和p2执行完之后,主进程才结束
    p1.join()
    p2.join()
