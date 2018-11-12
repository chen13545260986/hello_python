import socket

# 实例化socket对象
sk = socket.socket(type=socket.SOCK_DGRAM)

# 向指定的地址发送UDP数据
sk.sendto(b'hello',('127.0.0.1',8080))

# 接收UDP数据，以及发送数据的地址
msg,addr = sk.recvfrom(1024)
print(msg.decode('utf-8'))