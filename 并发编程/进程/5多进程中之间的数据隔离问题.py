from multiprocessing import Process

n = 100

def func():
    global n
    n = 0
    print('one:',n)


if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    p.join()
    print('two:',n)