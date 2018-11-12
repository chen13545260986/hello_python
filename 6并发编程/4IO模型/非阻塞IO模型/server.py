import socket

# 实例化socket
sk = socket.socket()

# 绑定地址并监听
sk.bind(('127.0.0.1',8080))
sk.listen(5)

# 把socket当中所有需要阻塞的方法改为非阻塞:recv recvfrom accept
sk.setblocking(False)

# 用来存储所有来请求server端的conn连接
conn_lst = []
# 用来储存所有已经断开与server端连接的conn
conn_del = []
while True:
    try:
        # 等待客户端连接
        conn,addr = sk.accept()
        print('%s建立了连接' % str(conn))
        # 将连接中的客户端放入到conn_lst列表中
        conn_lst.append(conn)
    except BlockingIOError:
        try:
            # 接收连接中的客户端发送的消息
            for i in conn_lst:
                msg = i.recv(1024)
                if msg == b'' or msg == b'q':
                    # 如果客服端下线，就将该客户端放入conn_del列表
                    conn_del.append(i)
                    i.send(b'bye!')
                    print('%s退出了连接' % str(i))
                    continue
                print(msg.decode('utf-8'))
            # 移除已经下线的客户端
            for i in conn_del:
                conn_lst.remove(i)
            # 清空处理过后的conn_del列表
            conn_del.clear()
        except BlockingIOError:
            pass