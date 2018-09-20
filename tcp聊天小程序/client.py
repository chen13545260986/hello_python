# 导入socket模块
import socket

# 创建socket对象
client = socket.socket()

# 连接socket
client.connect(('127.0.0.1', 8888))
# 向服务端发送一条消息
client.send(('你好，我是client').encode('utf-8'))
# 开启循环
while True:
    # 接收服务端发来的信息
    msg_s = client.recv(1024).decode('utf-8')
    print(len(msg_s))
    print('服务端发来消息:', msg_s)

    # 给服务端发信息
    msg = input('请输入:')
    client.send(msg.encode('utf-8'))

print(123)
