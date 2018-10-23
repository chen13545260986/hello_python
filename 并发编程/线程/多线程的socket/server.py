import socket
from threading import Thread

def func(c):
    # 给客户端发消息
    c.send(b'hello')

    # 接收客户端的消息
    msg = c.recv(1024).decode('utf-8')
    print(msg)

    # 关闭连接
    c.close()

# 起服务
sk = socket.socket()

# 绑定地址并监听
sk.bind(('127.0.0.1',8080))
sk.listen(5)

while True:
    # 等待客服端连接(在有连接进来之前代码会阻塞在这里)
    conn, addr = sk.accept()

    # 客户端连接之后，后续操作采用线程方式执行
    t = Thread(target=func,args=(conn,))
    t.start()

# 关闭socket
sk.close()