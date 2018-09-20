# 导入模块
import socket

# 创建socket对象
sk = socket.socket(type=socket.SOCK_DGRAM)

# 绑定连接
sk.bind(('127.0.0.1', 8888))

# 接收UDP数据,与recv()类似，但返回值是（data,address）
data, address = sk.recvfrom(1024)
print(data, address)

# 发送UDP数据
sk.sendto(b'hello', address)

# 关闭连接
# sk.close()

