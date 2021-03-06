import socket
import subprocess

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

    # 先把结果的长度发送过去
    coon.send(bytes(str(num),encoding='gbk'))

    # 收到确认
    sure = coon.recv(1024)
    if sure.decode('gbk') == 'ok':
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