#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   udp_socketClient.py
@Time    :   2019/06/27 09:41:00
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
import socket 

# socket.SOCK_DGRAM 指定是UDP协议
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))
# UDP不需要启动监听
print('Bind UDP on 9999...')

#
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)