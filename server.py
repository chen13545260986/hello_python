#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 导入 socket 常用模块
import socket

# 创建 socket 对象
s = socket.socket()
# 获取本地主机名
host = '127.0.0.1'
# 设置端口
port = 12345
# 绑定端口
s.bind((host, port))

# 等待客户端连接
s.listen(2)

while True:
    # 建立客户端连接
    c, addr = s.accept()
    print('连接地址:', addr)
    print(c)
    # 给客户端发送信息
    c.send(b'hello client')
    # 输出客户端发过来的信息
    print(c.recv(1024))


