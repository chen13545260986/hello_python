"""
logging:日志模块
    5种日志级别:debug,info,warning,error,critical
    2种配置方式：basicconfig,logger
"""
import logging

"""
basicconfig:简单 能做的事情相对少
    中文的乱码问题
    不能同时往文件和屏幕上输出
"""
# logging.basicConfig(
#     level= logging.WARNING,
#     format= '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s : %(message)s',
#     datefmt= '%a, %d %b %Y %H:%M:%S'
# )
# try:
#     int(input('>>>'))
# except ValueError:
#     logging.error('输入的值不是一个数字')
#
# logging.info('hello world')

"""
logger
"""
logger = logging.getLogger()
# 创建一个文件日志对象
fh = logging.FileHandler('test.log', encoding='utf-8')
# 创建一个格式
fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s [line:%(lineno)d] : %(message)s')
# 文件对象和格式关联
fh.setFormatter(fmt)
# logger对象和文件关联
logger.addHandler(fh)
logging.info('hello world')
logging.warning('警告错误')
logging.error('error message')
logging.critical('critical message')