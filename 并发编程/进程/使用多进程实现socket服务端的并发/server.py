import socket
from multiprocessing import Process

def myServer(connect,address):
        print('欢迎：%s' % str(address))
        # 给客户端发信息
        connect.send('欢迎光临！'.encode('utf-8'))
        # 接收客户端的消息
        msg = connect.recv(1024)
        print(msg.decode('utf-8'))


if __name__ == '__main__':
    # 实例化socket对象
    sk = socket.socket()

    # 绑定地址并监听
    sk.bind(('127.0.0.1', 8090))
    sk.listen(5)

    while True:
        # 等待客户端连接
        coon, addr = sk.accept()
        # 启动进程
        p = Process(target=myServer,args=(coon, addr))
        p.start()