from threading import Thread,Event
import time,random

def func1(e):
    count = 0
    while count < 3:
        count += 1
        if not e.is_set():
            # 当事件的状态为False时，阻塞1秒
            e.wait(1)
            print('第%s连接数据库失败' % count)
        else:
            print('第%s连接数据库成功' % count)
            break
    else:
        raise TimeoutError('连接超时')

def func2(e):
    time.sleep(random.randint(1,5))
    # 将事件的在状态设置为True
    e.set()

# 实例化事件对象
event = Event()
# 创建两个线程分别执行func1和func2方法
t1 = Thread(target=func1,args=(event,))
t2 = Thread(target=func2,args=(event,))
# 执行这两个线程
t1.start()
t2.start()