# 导入socket模块
import socket
import os
import hashlib

# 创建socket对象
server = socket.socket()
# 设置socket
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定地址
server.bind(('127.0.0.1', 8888))
# 开始TCP监听
server.listen(5)

# 循环
while True:
    # 接受TCP客户端连接
    print('开始监听...')
    # 接收并建立与客户端的连接，程序在此处开始阻塞，只有等到客户端连接进来开始往下执行
    coon, address = server.accept()
    print('有新的连接:', address)
    while True:
        # 接收到客户端的byte类型
        cmd = coon.recv(1024).decode('utf-8')
        print("收到消息 : ", cmd)

        if (len(cmd.split())) == 1:  # 如果是linux命令
            data = os.popen(cmd).read()
            if len(data) == 0:
                data = "来自客户端的cmd命令不存在"
            print(data)
            length = len(data.encode("utf-8"))  # 计算cmd命令结果的bytes长度
            coon.send(str(length).encode("utf-8"))  # 服务端向客户端发送cmd命令返回值的长度，因为客户端一次接收的数据量有限，需要知道长度，从而确定几次接受完
            print("nianbao:", coon.recv(1024).decode())
            coon.send(data.encode("utf-8"))

        if (len(cmd.split())) > 1:
            fname = cmd.split()
            if fname[0].startswith('get'):
                # 客户端要下载文件
                if os.path.isfile(fname[1]):
                    total_size = os.stat(fname[1]).st_size  # 返回文件的总byte长度
                    coon.send(str(total_size).encode("utf-8"))
                    coon.recv(1024)
                    m = hashlib.md5()
                    with open(fname[1], 'rb') as fr:
                        for line in fr:
                            coon.send(line)
                            m.update(line)
                    print(coon.recv(1024).decode())
                    coon.send(m.hexdigest().encode("utf-8"))
                else:
                    print("file is not exist")
                    coon.send(b"file is not exist")

        if not cmd:  # 如果客户端断开，一面服务端进入死循环
            print("client has interrupt")
            break

    print(123)
    coon.close()

print(456)
server.close()

