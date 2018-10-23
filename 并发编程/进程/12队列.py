from multiprocessing import Process
from multiprocessing import Queue

def func1(q):
    q.put('hello')


def func2(q):
    print(q.get())


if __name__ == '__main__':
    # 创建一个队列
    queue = Queue()
    # 创建一个进程来执行func1方法
    p1 = Process(target=func1,args=(queue,))
    p1.start()
    # 创建另一个进程来执行func2方法
    p2 = Process(target=func2,args=(queue,))
    p2.start()