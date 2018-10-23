"""
hashlib模块:提供摘要(加密)算法的模块
    对于相同的字符串使用同一个算法进行摘要，得到的值总是不变的
    sha算法随着算法复杂程度的增加，摘要的时间成本空间成本都会增加
用途：
    密码的密文存储
    文件的一致性验证
        在下载的时候 检查我们下载的文件和远程服务器上的文件是否一致
        两台机器上的两个文件 你想检查这两个文件是否相等
"""
import hashlib

# 被加密的字符串
str = 'abc'
# 实例化md5对象
md5 = hashlib.md5()
# 加密过程
md5.update(bytes(str, encoding='utf-8'))
# 获取加密结果
res = md5.hexdigest()
print(res)
print('=====')

"""
加盐
"""
str2 = 'daf'
md5_2 = hashlib.md5(b'salt')
md5_2.update(bytes(str,encoding='utf-8'))
print(md5_2.hexdigest())
print('=====')

"""
动态加盐
"""