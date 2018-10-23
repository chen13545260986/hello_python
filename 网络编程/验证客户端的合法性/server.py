"""
检测客户端是否合法:hmac模块
"""
import socket
import hmac
import os

# 密钥
secret_key = b'hello'

# 实例化
sk = socket.socket()

# 绑定地址和端口,并监听
sk.bind(('127.0.0.1',8080))
sk.listen(5)

while True:
    # 等待客户端连接
    print('等待客户端连接中...')
    coon,addr = sk.accept()
    print('%s,已连接' % str(addr))

    # 发送给客户端一段32位的字节信息
    msg = os.urandom(32)
    coon.send(msg)

    # 比对本地和客户端的密文
    h = hmac.new(secret_key,msg)
    digest = h.digest()
    digest_client = coon.recv(1024)
    res = hmac.compare_digest(digest,digest_client)

    if res:
        print('客户端合法')
    else:
        print('客户端不合法')
        break