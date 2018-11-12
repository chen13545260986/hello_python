"""
服务端
"""
import socket
import gevent
from gevent import monkey
monkey.patch_all()

def func(c,a):
    # 给c发送信息
    c.send(b'welcome to connect!')
    # 接收来自c的信息
    msg = c.recv(1024).decode('utf-8')
    print('%s :%s' % (str(a),msg))


# 实例化socket
sk = socket.socket()

# 绑定地址并监听
sk.bind(('127.0.0.1',8080))
sk.listen(5)

while True:
    # 等待客户端连接(会阻塞)
    conn,addr = sk.accept()
    # 客户端连接之后的操作，采用协程处理
    g = gevent.spawn(func,conn,addr)