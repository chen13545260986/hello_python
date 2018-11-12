"""
客户端
"""
import socket

# 实例化socket
sk = socket.socket()

# 连接服务端
sk.connect(('127.0.0.1',8080))

# 接收服务端的消息
msg = sk.recv(1024).decode('utf-8')
print(msg)

# 给服务端发消息
info = input('>>>').encode('utf-8')
sk.send(info)

# 关闭连接
sk.close()