from threading import Timer

def func():
    print(123)

Timer(3,func).start()