from multiprocessing import Pipe
from multiprocessing import Process

def func(c1,c2):
    c1.close()
    while True:
        try:
            data = c2.recv()
            print(data)
        except EOFError:
            c2.close()
            break


if __name__ == '__main__':
    # 实例化管道
    conn1,conn2 = Pipe()
    # 创建进程并开启
    Process(target=func,args=(conn1,conn2)).start()
    for i in range(10):
        conn1.send(123)
    conn1.close()
    conn2.close()