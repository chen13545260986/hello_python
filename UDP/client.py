# 导入模块
import socket

# 创建socket客户端对象
client = socket.socket(type=socket.SOCK_DGRAM)

# 直接给服务器发送一段消息
client.sendto(b'hello,i am client', ('127.0.0.1', 8888))

# 接收对面的回信
msg, address = client.recvfrom(1024)
print(msg.decode(), address)
