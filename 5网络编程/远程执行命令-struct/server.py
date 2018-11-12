import socket
import subprocess
import struct

# 实例化
sk = socket.socket()

# 绑定地址和端口
sk.bind(('127.0.0.1', 8080))

# 监听,最大连接数为5
sk.listen(5)

# 接收连接
coon, addr = sk.accept()

while True:
    # 接收到的cmd命令
    cmd = coon.recv(1024).decode('gbk')
    if cmd == 'q':
        break

    # 执行该cmd命令
    res = subprocess.Popen(cmd,shell=True,
                           stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    # 获取返回的结果
    res_stdout = res.stdout.read()
    res_stderr = res.stderr.read()
    num = len(res_stdout)+len(res_stderr)

    # 将num转成特定(4)位数的bytes类型
    num = struct.pack('i',num)

    # 先发送4个字节，告诉客户端结果的长度
    coon.send(num)

    # 再发送结果信息
    coon.send(res_stdout)
    coon.send(res_stderr)


# 关闭连接
coon.close()

# 关闭socket对象
sk.close()

"""
将结果的长度发回的好处：
    确定了客户端要接收多大的数据，从而一次就接收完
坏处：
    多了一次交互过程
"""