"""
检测客户端是否合法:hmac模块
"""
import socket
import hmac

# 密钥
secret_key = b'hello'

# 实例化
sk = socket.socket()

# 连接地址
sk.connect(('127.0.0.1',8080))

# 接收服务端发送来的明文
res1 = sk.recv(32)

# 加密后发送给服务端
h = hmac.new(secret_key,res1)
digest = h.digest()
sk.send(digest)