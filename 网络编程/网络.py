# python基础
# 网络编程 _ 概念  4天
# 什么是网络 网络的基础概念 *****
# socket
# TCP
# UDP
# 并发编程 _ 概念
# 一天


# qq 微信 飞秋 网游 微博 歪歪  _基于应用的网络程序
# 百度 微博 知乎 博客园 网易   _基于浏览器的网络程序

# 网络编程中的 - C/S架构
# c client  客户端
# s server  服务端
# 网络编程中的 - B/S架构
# b broser  浏览器
# s server  服务端
# 不需要额外的安装客户端了,只需要一个网址就可以访问
# 轻量级  - 使用成本低
# B/S架构是C/S架构的一种特殊形式
# 手机上 : 浏览器 app

# 两个py程序想要通信
# 写文件
# 在不同机器上的两个py程序之间想要通信
# 网络

# 网络的发展史
# 网卡\网口
# 两台机器之间 插上网线就可以通信
# 网卡上 - mac地址
# ip地址
# 是4个点分十进制  - ipv4协议
# 0.0.0.0 - 255.255.255.255
# 127.0.0.1 本机
# 内网字段 192.168.****
#  10.****
#  172.***
# 6个点分十进制  - ipv6协议
# 0.0.0.0.0.0  - 255.255.255.255.255.255
# 交换机
# 广播
# 单播
# 组播
# arp协议 : 通过IP地址获取某一台机器的mac地址
# 子网掩码
# 子网掩码 和 ip地址进行 按位 与 运算 就能得出一个机器所在的网段
# 192.168.21.36
# 11000000.10101000.00010101.00100100
# 255.255.255.0   255.255.0.0
# 11111111.11111111.11111111.00000000
# 11000000.10101000.00010101.00000000
# 192.168.21.0 网段
# 网关地址 : 整个局域网中的机器能沟通过网关ip与外界通信
# 网段 : 子网掩码 和 ip地址进行 按位 与 运算
# 端口 : 0-65535
# 8000-酷狗音乐  22-ssh  3306-mysql
# python 网络应用  8000
# ip地址+端口号 : 在全网找到唯一的一台机器+唯一的应用
# 我们选择端口 : 8000之后
# tcp协议
# 全双工的通信协议
# 一旦连接建立起来,那么连接两端的机器能够随意互相通信
# 面向连接的通信方式
# 数据安全不容易丢失
# 建立连接的 三次握手 ******
# 断开连接的 四次挥手 ******
