"""
一个信号可以使所有进程都进入阻塞状态
也可以控制所有的进程解除阻塞
一个事件被创建之后，默认是阻塞状态
is_set():查看一个事件的装填，默认被设置为阻塞
wait():依据e.is_set()的值来决定是否阻塞,为False阻塞，True不阻塞
set():将一个事件的状态改为True
clear():将一个事件的状态改为False
"""
from multiprocessing import Event

e = Event()
e.set()
print(e.is_set())
e.wait()
print(1)
e.clear()
print(e.is_set())
e.wait()
print(2)