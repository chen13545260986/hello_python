from multiprocessing import Process
from multiprocessing import Lock
import json
import time

# 购票
def buy(n,l):
    # 开启进程锁
    l.acquire()

    # 看看是否还有票
    with open('ticket') as f:
        dic = json.load(f)
        time.sleep(0.1)

    if dic['ticket'] > 0:
        # 更新余票
        dic['ticket'] -= 1
        with open('ticket','w') as f2:
            json.dump(dic,f2)
        print('%s:买到票了' % n)
    else:
        print('%s:没买到票' % n)

    # 结束锁
    l.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p = Process(target=buy,args=(i,lock))
        p.start()