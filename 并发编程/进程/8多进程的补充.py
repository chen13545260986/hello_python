"""
子进程里面不能有input
"""
from multiprocessing import Process

def func():
    # input('>>>')
    print(123)


if __name__ == '__main__':
    Process(target=func).start()