import select
import socket

# 实例化socket
sk = socket.socket()

# 绑定地址并监听
sk.bind(('127.0.0.1',8080))
# 设置为非阻塞IO
sk.setblocking(False)
sk.listen(5)

# 被代理的列表对象
lst = [sk]

while True:
    rlist, wlist, xlist = select.select(lst, [], [])

    # 遍历被代理的列表对象
    for i in rlist:
        if i == sk:
            conn,addr = i.accept()
            # 将连接追加到被代理的列表中
            lst.append(conn)
        else:
            msg = i.recv(1024)
            if msg == b'':
                i.close()
                lst.remove(i)
                continue
            print(msg)

# 关闭socket
sk.close()