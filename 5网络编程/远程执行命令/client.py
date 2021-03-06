import socket

# 实例化
sk = socket.socket()

# 连接
sk.connect(('127.0.0.1',8080))

while True:
    # 获取输入
    cmd = input('>>>')
    # q为退出
    if cmd == 'q':
        break
    # 发送命令到服务端
    sk.send(bytes(cmd,encoding='gbk'))

    # 先接收返回的长度信息
    num = sk.recv(1024)

    # 返回确认
    sk.send(b'ok')

    # 再接收结果信息
    msg = sk.recv(int(num))
    print(msg.decode('gbk'))

