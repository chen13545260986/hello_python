import socket

# 实例化socket对象
sk = socket.socket(type=socket.SOCK_DGRAM)

# 绑定地址和端口
sk.bind(('127.0.0.1',8080))

# 接收UDP数据，以及发送数据的地址
msg,addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))

# 向指定的地址发送UDP数据
sk.sendto(b'welcome to connect',addr)

# 关闭socket
sk.close()

"""
UDP：不黏包，容易丢失数据
TCP：黏包，不会丢失数据
"""