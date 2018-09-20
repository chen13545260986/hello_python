# try-finally 语句无论是否发生异常都将执行最后的代码。

try:
    file = open('test.txt', 'r+')
except IOError:
    print('没有该文件')
else:
    print('没有异常')
finally:
    print('执行完毕')