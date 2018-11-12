import socket

# 创建socket
sk = socket.socket()

# 连接指定地址
sk.connect(('127.0.0.1',8080))

# 接收消息
msg = sk.recv(1024).decode('utf-8')
print(msg)

# 发消息
info = input('>>>')
sk.send(info.encode('utf-8'))