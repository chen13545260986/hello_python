"""
socketserver模块：允许多个客户端连接的模块
"""
import socketserver

# 服务端类
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        # 向客户端打招呼
        self.request.send(b'welcome to connect')

        while True:
            # 接收客户端发来的信息
            msg = self.request.recv(1024)
            print(msg.decode('utf-8'))

            # 回消息
            # info = input('>>>')
            # self.request.send(info.encode('utf-8'))


# 实例化并启动服务端
server = socketserver.ThreadingTCPServer(('127.0.0.1',8080), MyServer)
server.serve_forever()