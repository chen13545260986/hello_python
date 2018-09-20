#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 导入 socket 常用模块
import socket

# 创建 socket 对象
s = socket.socket()
# 获取本地主机名
host = '127.0.0.1'
# 设置端口号
port = 12345

# 连接socket对象
s.connect((host, port))

# 输出服务端发来的消息
print(s.recv(1024))

# 给服务端发送信息
s.send(b'hello server1')
# 关闭连接
s.close()

