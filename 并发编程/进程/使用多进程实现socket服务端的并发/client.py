import socket

# 实例化socket对象
sk = socket.socket()

# 连接
sk.connect(('127.0.0.1',8090))

# 接收服务端发来的消息
msg = sk.recv(1024)
print(msg.decode('utf-8'))

# 给服务端发信息
info = input('>>>')
sk.send(info.encode('utf-8'))