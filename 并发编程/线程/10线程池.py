from concurrent.futures import ThreadPoolExecutor
import time

def func(n):
    time.sleep(0.5)
    print(n)
    return n*n

# 创建线程池
pool = ThreadPoolExecutor(max_workers=5)    # 默认不要超过CPU的个数乘以5
t_lst = []
# 创建10个子线程执行func
for i in range(10):
    t = pool.submit(func,i)
    t_lst.append(t)
# close+join
pool.shutdown()
# 循环输出子线程的结果
for t in t_lst:
    print('***',t.result())