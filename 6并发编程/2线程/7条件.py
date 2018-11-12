from threading import Condition,Thread

def func(c,n):
    c.acquire()
    # 等钥匙
    c.wait()
    print('第%s次循环中' % n)
    c.release()

# 实例化条件类
con = Condition()
# 创建10个线程分别执行func方法
for i in range(10):
    t = Thread(target=func,args=(con,i)).start()
while True:
    num = int(input('>>>'))
    con.acquire()
    # 造钥匙,num表示钥匙的数量
    con.notify(num)
    con.release()