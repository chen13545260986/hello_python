import socket

# 实例化socket
sk = socket.socket()

# 建立连接
sk.connect(('127.0.0.1',8080))

# 给服务端发消息
sk.send(b'hello!')

while True:
    info = input('>>>')
    sk.send(info.encode('utf-8'))
    if info == 'q':
        # 接收服务端的消息
        msg = sk.recv(1024)
        print(msg.decode('utf-8'))
        break

# 关闭连接
sk.close()