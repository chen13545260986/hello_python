import socket
import time

# 实例化socket对象
sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  # 避免服务器端重启时报address already in use

# 绑定ip和端口
sk.bind(('127.0.0.1',8080))

# 监听
sk.listen(2)  # 允许几个人连接
print('waiting client to connect...')

# 获取连接的对象和地址
coon,addr = sk.accept()     # 阻塞：等待连接进来，直到有人连接为止
# print('coon:',coon)
# print('addr:',addr)

# 给coon对象发消息
coon.send(b'welcome to connect')

while True:
    # 接收coon对象发过来的信息
    msg = coon.recv(1024).decode('utf-8')   # 1024为数据的大小限制,程序未接收到信息会发生阻塞，直到收到信息为止
    if msg == 'bye':
        break
    # 发送消息给客户端
    msg = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(float(msg)))
    coon.send(bytes(msg,encoding='utf-8'))

# 关闭coon连接
coon.close()

# 关闭socket对象
sk.close()