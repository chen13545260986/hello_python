from multiprocessing import Process
import os

def func(args):
    print('子进程：',os.getpid())
    print('子进程的父进程：',os.getppid())
    print(12345)
    print(args)


# windows系统使用必须的条件，其他系统可以直接使用
if __name__ == '__main__':
    # 注册
    p = Process(target=func,args=(54321,))  # p是一个进程对象，还没有启动

    # 启动进程
    p.start()
    # 查看当前进程号
    print('当前进程：',os.getpid())
    print('父进程：',os.getppid())