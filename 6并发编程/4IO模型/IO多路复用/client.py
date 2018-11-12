import socket
from threading import Thread

def func():
    # 实例化socket
    s = socket.socket()

    # 连接地址
    s.connect(('127.0.0.1', 8080))

    # 给server发消息
    s.send(b'hello')

    # 关闭连接
    s.close()

# func(sk)

for i in range(10):
    t = Thread(target=func)
    t.start()