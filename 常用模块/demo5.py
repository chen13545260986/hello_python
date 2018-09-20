# os模块
import os

# 创建目录
# os.mkdir('test', 777)

# 打开文件
file = os.open('test/test.txt', os.O_RDWR)

# 写入
str = 'hello world'
os.write(file, str.encode('utf-8'))

# 关闭文件
os.close(file)