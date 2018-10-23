import threading
import time

def func(n):
    time.sleep(0.1)
    print(n,threading.current_thread(),threading.get_ident())

for i in range(10):
    t = threading.Thread(target=func,args=(i,))
    t.start()

# 当前正在运行的线程（包括主线程）
print(threading.active_count())
# 获取当前线程
print(threading.current_thread())
print(threading.enumerate())