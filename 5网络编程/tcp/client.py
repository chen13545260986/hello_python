import socket
import time

# 实例化socket对象
sk = socket.socket()

# 连接服务端
sk.connect(('127.0.0.1',8080))

while True:
    # 接收服务端发来的消息
    msg = sk.recv(1024).decode('utf-8')
    if msg == 'bye':
        break
    print('\r%s' % msg,end='')
    time.sleep(1)
    # 发送消息给服务端
    info = time.time()
    sk.send(bytes(str(info),encoding='utf-8'))

# 关闭连接
sk.close()