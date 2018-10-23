"""
configparse模块
"""
import configparser

"""
创建配置文件
"""
# 实例化
# config = configparser.ConfigParser()
# 设置内容
# config['default'] = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }
# config['db'] = {
#     'host': '127.0.0.1',
#     'port': 3306
# }
# 写入配置文件
# with open('config.ini','w') as f:
#     config.write(f)

"""
读取配置文件
"""
# config2 = configparser.ConfigParser()
# print(config2.sections())
# # 读取配置文件
# config2.read('config.ini')
# # 获取配置文件节点
# print(config2.sections())
# # 判断该配置文件对象中是否有该节点
# print('db' in config2)
# print('log' in config2)
# # 获取配置文件中对应节点中对应键的值
# print(config2['db']['host'])
# for k in config2['db']:
#     print(k)
#
# # 获取对应节点的所有键
# print(config2.options('default'))
# # 获取对应节点的键值对
# print(config2.items('db'))
# # 获取对应节点对应键的值
# print(config2.get('db', 'host'))

"""
修改配置文件
"""
config = configparser.ConfigParser()
config.read('config.ini')   # 读文件
config.add_section('yuan')   # 增加section
config.remove_section('bitbucket.org')   # 删除一个section
config.remove_option('topsecret.server.com',"forwardx11")  # 删除一个配置项
config.set('topsecret.server.com','k1','11111')
config.set('yuan','k2','22222')
f = open('new2.ini', "w")
config.write(f) # 写进文件
f.close()