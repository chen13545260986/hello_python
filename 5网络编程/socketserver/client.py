import socket

# 实例化
sk = socket.socket()

# 连接
sk.connect(('127.0.0.1',8080))

# 接收服务端发来的信息
msg = sk.recv(1024)
print(msg.decode('utf-8'))

while True:
    # 给服务端发信息
    data = input('>>>')
    if data == 'q':
        break
    sk.send(('client1:'+data).encode('utf-8'))

    # 接收信息
    # msg2 = sk.recv(1024)
    # print(msg2.decode('utf-8'))

# 关闭连接
sk.close()