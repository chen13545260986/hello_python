"""
自定义一个类，并且继承Process类，同时申明一个run方法
"""
from multiprocessing import Process

class MyProcess(Process):
    def run(self):
        print(123)

if __name__ == '__main__':
    p = MyProcess()
    p.start()