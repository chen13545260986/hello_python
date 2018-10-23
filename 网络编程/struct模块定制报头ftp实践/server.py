import socket
import struct
import json
import os

buffer = 4096

# 实例化socket
sk = socket.socket()

# 绑定地址和端口
sk.bind(('127.0.0.1',8080))

# 监听
sk.listen(5)

print('等待客户端连接...')

while True:
    # 获取连接对象
    coon,addr = sk.accept()
    print('有一个地址为：%s，的客户端连接中...' % str(addr))

    # 先接收头信息的大小
    res1 = coon.recv(4)
    head_len = struct.unpack('i',res1)[0]

    # 再接收头信息
    head_bytes = coon.recv(head_len)
    head_str = head_bytes.decode('utf-8')

    # 处理头信息
    head = json.loads(head_str)

    # 打开一个新的文件
    fileName = os.path.basename(head['fileName'])
    fileSize = head['fileSize']
    with open(fileName,'wb') as f:
        while fileSize:
            if fileSize > buffer:
                content = coon.recv(buffer)
                f.write(content)
                fileSize -= buffer
            else:
                content = coon.recv(fileSize)
                f.write(content)
                fileSize = 0

    # 返回文件的新地址
    pwd = os.getcwd()
    newPath = os.path.join(pwd,fileName)
    coon.send(bytes(newPath,encoding='utf-8'))

    # 关闭连接和socket
    coon.close()
    print('连接已断开')