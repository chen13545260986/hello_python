import socket
import struct
import json
import os

# 每次读取的文件字节大小
buffer = 4096

# 实例化socket
sk = socket.socket()

# 连接服务器
sk.connect(('127.0.0.1',8080))

# 文件信息
fileName = input('请输入要上传的文件:')

# 获取文件的大小
fileSize = os.path.getsize(fileName)

# 头信息列表
lst = {
    'fileName': fileName,
    'fileSize': fileSize
}
# 将头信息转成json字符串
lst_josn = json.dumps(lst,ensure_ascii=False)
lst_len = len(bytes(lst_josn,encoding='utf-8'))

# 将头信息的大小传过去
head_len = struct.pack('i',lst_len)
sk.send(head_len)

# 将头信息传过去
head = lst_josn.encode('utf-8')
sk.send(head)

print('文件上传中...')
# 再将文件传过去
with open(fileName,'rb') as f:
    while fileSize:
        if fileSize > buffer:
            # 每次读取这么多字节的数据
            content = f.read(buffer)
            # 发送给服务端
            sk.send(content)
            fileSize -= buffer
        else:
            content = f.read(fileSize)
            sk.send(content)
            fileSize = 0

print('文件上传成功')

# 接收返回的上传文件的地址
newFileName = sk.recv(1024).decode('utf-8')
print('新文件的地址为：%s' % newFileName)

# 关闭socket
sk.close()