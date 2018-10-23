from threading import Thread,Semaphore
import time

def func(s,a,b):
    s.acquire()
    time.sleep(1)
    print(a+b)
    s.release()

# 实例化信号量
sem = Semaphore(4)
# 创建10个线程并执行
for i in range(10):
    t = Thread(target=func,args=(sem,i,i*10))
    t.start()